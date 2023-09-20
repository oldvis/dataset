"""
Utility functions to build "author" entities.
"""

import re
from typing import Dict, List, Tuple, TypedDict, Union

from libprocess.typing import ProcessedMetadataEntry
from typing_extensions import NotRequired

from .rules.replace_substring import rules as _rules_replace_substring

rules_replace_substring = {
    d["substring"]: d["replaceWith"] for d in _rules_replace_substring
}


class TimePoint(TypedDict):
    year: int
    month: NotRequired[int]
    day: NotRequired[int]


class Lifespan(TypedDict):
    birth: Union[TimePoint, List[TimePoint], None]
    death: Union[TimePoint, List[TimePoint], None]


class Author(TypedDict):
    name: str
    birth: Union[TimePoint, List[TimePoint], None]
    death: Union[TimePoint, List[TimePoint], None]
    occupation: Union[str, None]
    # The input string from which the author is parsed.
    input: str


def replace_substrings(name_str: str) -> str:
    """
    Clean the name string by replacing substrings according to rules.
    """

    rules = rules_replace_substring
    name = name_str
    for name_raw in rules:
        if name_raw in name:
            name = name.replace(name_raw, rules[name_raw])
    return name


def parse_year_with_dot(year_str: str) -> Union[TimePoint, List[TimePoint], None]:
    """
    Parse year strings with dot.

    Example:
    - input: "18.."
    - output: [{"year": 1800}, {"year": 1899}]
    """

    m = re.findall(r"\d{1,4}[.]{0,3}", year_str)
    if len(m) == 0:
        return None

    n_dots = m[0].count(".")
    year = int(re.findall(r"\d{1,4}", m[0])[0])
    if n_dots == 0:
        return {"year": year}
    if n_dots == 1:
        return [{"year": year * 10}, {"year": year * 10 + 9}]
    if n_dots == 2:
        return [{"year": year * 100}, {"year": year * 100 + 99}]
    if n_dots == 3:
        return [{"year": year * 1000}, {"year": year * 1000 + 999}]
    return None


def split_lifespan(name_str: str) -> Tuple[str, Union[Lifespan, None]]:
    """
    Parse date of birth and death from name string.
    """

    # Rules (for David Rumsey Map Collection):
    if name_str == "Aspin, Jehoshaphat, 18th/19th cent.":
        return "Aspin, Jehoshaphat", {
            "birth": [None, {"year": 1799}],
            "death": [{"year": 1800}, None],
        }

    # Examples (in David Rumsey Map Collection):
    # - Cook, James, active 1762-1775
    m = re.findall(r", active \d+-\d+", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": [None, {"year": int(years[0])}],
            "death": [{"year": int(years[1])}, None],
        }

    # Examples (in David Rumsey Map Collection):
    # - Smith, Charles, fl. 1800-1822
    m = re.findall(r", fl. \d+-\d+", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": [None, {"year": int(years[0])}],
            "death": [{"year": int(years[1])}, None],
        }

    # Examples (in David Rumsey Map Collection):
    # - Savigny, Christophe de, approximately 1530-1608
    m = re.findall(r", approximately \d+-\d+", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": {"year": int(years[0])},
            "death": {"year": int(years[1])},
        }

    # Examples (in David Rumsey Map Collection):
    # - Stucchi, Stanislao (approximately 1780)
    m = re.findall(r" (approximately \d+)", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": [None, {"year": int(years[0])}],
            "death": [{"year": int(years[1])}, None],
        }

    # Examples (in David Rumsey Map Collection):
    # - Cary, John, ca. 1754-1835
    m = re.findall(r", ca. \d+-\d+", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": {"year": int(years[0])},
            "death": {"year": int(years[1])},
        }

    # Examples (in David Rumsey Map Collection):
    # - Luffman, John, 1756-1846
    # - Hawkesworth, John, 1715?-1773
    # - Coronelli, Vincenzo (1650-1718)
    # - Schlieben, Wilhelm Ernst August von (1781 - 1839)
    m = re.findall(r"[,]*\s*\(*[\d?]+\s*[\-–]\s*\d+\)*", name_str)
    if len(m) == 1:
        # year_str example: ", 1756-1846"
        year_str = m[0]
        years = re.findall(r"\d+", year_str)
        if not (
            len(years) != 2 or (not years[0].isdigit()) or (not years[1].isdigit())
        ):
            name = name_str.split(year_str)[0]
            return name, {
                "birth": {"year": int(years[0])},
                "death": {"year": int(years[1])},
            }

    # Examples (in David Rumsey Map Collection):
    # - Arnold, Thomas Jefferson, d. 1878
    m = re.findall(r", d. \d+", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": None,
            "death": {"year": int(years[0])},
        }

    # Examples (in Gallica):
    # - Hervieu, Jules (18..-19..)
    # - Wacquez-Lalo, Auguste (18..-1893)
    # - Aobus, Motonobu (17..?-18..)
    # - Flavius Josèphe (0038?-0100?)
    m = re.findall(r"\s*\([\d.]+[?]*\s*[\-]\s*.?[\d.]+.?\)", name_str)
    if len(m) == 1:
        year_str = m[0]
        name = name_str.split(year_str)[0]
        left, right = year_str.split("-")
        return name, {
            "birth": parse_year_with_dot(left),
            "death": parse_year_with_dot(right),
        }

    # Examples (in Internet Archive):
    # - Pratt, Edward Ewing, 1886-
    m = re.findall(r"[,]*\s*\(*[\d?]+\s*-\s*\d*\)*", name_str)
    if len(m) == 1:
        # year_str example: `, 1886-`
        year_str = m[0]
        name = name_str.split(year_str)[0]
        left, right = year_str.split("-")
        m_birth = re.findall(r"\d{1,4}", left)
        birth_year = None if len(m_birth) == 0 else int(m_birth[0])
        m_death = re.findall(r"\d{1,4}", right)
        death_year = None if len(m_death) == 0 else int(m_death[0])
        return name, {
            "birth": None if birth_year is None else {"year": birth_year},
            "death": None if death_year is None else {"year": death_year},
        }

    # Examples (in Library of Congress):
    # - Jefferys, Thomas, -1771.
    m = re.findall(r",\s*-\s*\d+.", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        year = re.findall(r"\d+", m[0])[0]
        return name, {
            "birth": None,
            "death": {"year": int(year)},
        }

    # Examples (in Library of Congress):
    # - Bernard, William Leigh, born 1845.
    m = re.findall(r", born \d+.", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        year = re.findall(r"\d+", m[0])[0]
        return name, {
            "birth": {"year": int(year)},
            "death": None,
        }

    # Examples (in Library of Congress):
    # - Frost, Horace Josiah, active 1878.
    m = re.findall(r", active \d+", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": [None, {"year": int(years[0])}],
            "death": [{"year": int(years[0])}, None],
        }

    # Examples (in Library of Congress):
    # - Reuter, Ferdinand, 1806.
    m = re.findall(r", \d+[.]", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": [None, {"year": int(years[0])}],
            "death": [{"year": int(years[0])}, None],
        }

    return name_str, {
        "birth": None,
        "death": None,
    }


def split_occupations(name_str: str) -> Tuple[str, List[str]]:
    """
    Parse occupations from name string.

    Returns
    -------
    - the name string with the occupation part remove
    - the parsed occupations.
    """

    # Rules and matched examples for Gallica:
    rules_gallica = {
        # - Minard, M. (18..-18..? ; ingénieur)
        " ; ingénieur": "engineer",
        # - Petit, Charles (18..-19.. ; inspecteur de l'enseignement primaire)
        "; inspecteur de l'enseignement primaire": "primary education inspector",
        # - Prévot, Victor (19..-.... ; agrégé d'histoire et de géographie)
        "; agrégé d'histoire et de géographie": "graduate in history and geography",
        # - Flavius Josèphe (0038?-0100?). Fonction indéterminée
        ". Fonction indéterminée": "Fonction indéterminée",
        # - Wautier d'Halluvin, Édouard (18..-18.. ; professeur d'histoire)
        " ; professeur d'histoire": "history teacher",
        # - Blumenthal, J. (18..-18.. ; géographe)
        " ; géographe": "geographer",
        # - Brion de La Tour, Louis (17..-18..-géographe)
        "-géographe": "geographer",
        # - Le Bourguignon-Duperré, Cyprien Gabriel (17..-18..?-hydrographe)
        "-hydrographe": "hydrographer",
        # - Ricard (18..?-18.. ; arpenteur forestier)
        " ; arpenteur forestier": "forest surveyor",
        # - Grange, C. (18..-.... ; agent-voyer). Dessinateur
        "; agent-voyer": "travel agent",
        # - Coste, Léon (ancien élève de l'École polytechnique, ingénieur des mines)
        ", ingénieur des mines": "mining engineer",
        # - La Pierre, Augustin Denis Édouard (lieutenant de vaisseau)
        " (lieutenant de vaisseau)": "first lieutenant",
        # - "Louis XIII (1601-1643 ; roi de France). Dédicataire"
        " ; roi de France": "king of France",
    }

    # Rules and matched examples for David Rumsey Map Collection:
    rules_david_rumsey_map_collection = {
        # - Aspioti-ELKA (Firm)
        "(Firm)": "firm",
    }

    # Rules and matched examples for Library of Congress:
    rules_library_of_congress = {
        # - Margolies, John, collector.
        ", collector": "collector",
        # - Bernard, William Leigh, born 1845 Compiler.
        " Compiler": "compiler",
    }

    rules = {
        **rules_gallica,
        **rules_david_rumsey_map_collection,
        **rules_library_of_congress,
    }

    name = name_str
    occupations = []
    for d in rules:
        if d not in name:
            continue
        name = name.replace(d, "")
        occupations.append(rules[d])

    return name, occupations


def split_roles(name_str: str) -> Tuple[str, List[str]]:
    """
    Parse roles from name string.
    Note: "roles" refers to the author's roles in the work, e.g., engraver, editor.

    Returns
    -------
    - the name string with the roles part remove
    - the parsed roles.
    """

    # Rules and matched examples for Gallica:
    rules_gallica = {
        # - Guérard, Nicolas (1648?-1719). Graveur
        ". Graveur": "engraver",
        " ; graveur": "engraver",
        "(graveur)": "engraver",
        # - Despujols, Pierre (18..-19..). Cartographe
        ". Cartographe": "cartographer",
        # - Mahaut (17..-18.. ; lithographe). Lithographe
        " ; lithographe": "lithographer",
        ". Lithographe": "lithographer",
        # - L'Illustration (Éditeur). Éditeur scientifique
        " (Éditeur)": "editor",
        ". Éditeur scientifique": "editor",
        # - Grange, C. (18..-.... ; agent-voyer). Dessinateur
        ". Dessinateur": "designer",
        # - Battista Agnese. Auteur présumé du texte
        ". Auteur présumé du texte": "presumed author of the text",
        # - Bauer, Eugène. Auteur du texte
        ". Auteur du texte": "author of the text",
        # - "Louis XIII (1601-1643 ; roi de France). Dédicataire"
        ". Dédicataire": "dedicatee",
    }

    # Rules and matched examples for David Rumsey Map Collection:
    rules_david_rumsey_map_collection = {
        # - Thomas, Joseph, publisher
        ", publisher": "publisher",
    }

    # Rules and matched examples for Library of Congress:
    rules_library_of_congress = {
        # - United States. Committee on Public Information, cartographer.
        ", cartographer.": "cartographer",
        # - Geological Survey (U.S.), contributor.
        ", contributor.": "contributor",
    }

    # Rules and matched examples for British Library Collection Items
    rules_british_library_collection_items = {
        # - Sir Anthony Ashley [translator]
        " [translator]": "translator",
        # - Lucas Janszoon Waghenaer [author]
        " [author]": "author",
        # - Mustafà, called Hikmet -'i San [scribe]
        " [scribe]": "scribe",
        # - W. & A.K. Johnston (cartographers)
        " (cartographers)": "cartographers",
    }

    rules = {
        **rules_gallica,
        **rules_david_rumsey_map_collection,
        **rules_library_of_congress,
        **rules_british_library_collection_items,
    }

    name = name_str
    roles = []
    for d in rules:
        if d not in name:
            continue
        name = name.replace(d, "")
        roles.append(rules[d])

    return name, roles


def build_author(name_str: str) -> Author:
    """
    Process the name string.
    """

    name = replace_substrings(name_str)
    name, occupations = split_occupations(name)
    name, roles = split_roles(name)
    name, lifespan = split_lifespan(name)
    return {
        "name": name.strip(),
        "birth": lifespan["birth"],
        "death": lifespan["death"],
        "occupations": occupations,
        "roles": roles,
        "input": name_str,
    }


def get_name2author(
    processed_metadata: List[ProcessedMetadataEntry],
) -> Dict[str, Author]:
    name_strs = []
    for d in processed_metadata:
        if d["authors"] is None:
            continue
        name_strs += d["authors"]
    name_strs = [*set(name_strs)]
    return {name_str: build_author(name_str) for name_str in name_strs}


def build_authors(processed_metadata: List[ProcessedMetadataEntry]) -> List[Author]:
    name2author = get_name2author(processed_metadata)
    authors = [*name2author.values()]
    authors = sorted(authors, key=lambda d: d["name"] + d["input"])
    return authors
