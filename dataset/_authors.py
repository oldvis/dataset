"""
Utility functions to build "author" entities.
"""

import re
from typing import Dict, List, Tuple, TypedDict, Union

from libprocess.typing import ProcessedMetadataEntry
from typing_extensions import NotRequired


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

    rules = {
        # For David Rumsey Map Collection:
        "Delamarche, Charles Fran��ois": "Delamarche, Charles François",
        "Colton, G. Woolworth": "Colton, George Woolworth",
        "Colton, G.W.": "Colton, George Woolworth",
        "Griffith, Richard John,; Sir;": "Griffith, Richard John",
        # For Gallica:
        # - "Auteur du texte" is "Author of the text" in French.
        ". Auteur du texte": "",
        # For Library of Congress:
        # - Reference: http://worldcat.org/identities/lccn-n2012077287/
        "Frost, H. J.": "Frost, Horace Josiah",
        # For Internet Archive:
        "Peter Jockisch, www.peterjockisch.de": "Peter Jockisch",
        # - 'Sloane, Charles S.' and 'Sloan, Charles S.' are the same person
        # and the latter name is more commonly used.
        "Sloan, Charles S.": "Sloane, Charles S.",
        "PLAYFAIR William": "Playfair, William",
    }

    name = name_str
    for name_raw in rules:
        if name_raw in name:
            name.replace(name_raw, rules[name_raw])
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

    # Examples (in David Rumsey Map Collection):
    # - "Cook, James, active 1762-1775"
    m = re.findall(r", active \d+-\d+", name_str)
    if len(m) == 1:
        name = name_str.split(m[0])[0]
        years = re.findall(r"\d+", m[0])
        return name, {
            "birth": [None, {"year": int(years[0])}],
            "death": [{"year": int(years[1])}, None],
        }

    # Examples (in David Rumsey Map Collection):
    # - "Savigny, Christophe de, approximately 1530-1608"
    m = re.findall(r", approximately \d+-\d+", name_str)
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

    return name_str, {
        "birth": None,
        "death": None,
    }


def split_occupation(name_str: str) -> Tuple[str, Union[str, None]]:
    """
    Parse occupation from name string.

    Returns
    -------
    - the name string with the occupation part remove
    - the parsed occupation.
    """

    # Rules and matched examples for Gallica:
    rules_gallica = {
        # - Guérard, Nicolas (1648?-1719). Graveur
        ". Graveur": "engraver",
        " ; graveur": "engraver",
        "(graveur)": "engraver",
        # - Minard, M. (18..-18..? ; ingénieur)
        " ; ingénieur": "engineer",
        # - Despujols, Pierre (18..-19..). Cartographe
        ". Cartographe": "cartographer",
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
        ". Dessinateur": "designer",
        "; agent-voyer": "travel agent",
        # - Coste, Léon (ancien élève de l'École polytechnique, ingénieur des mines)
        ", ingénieur des mines": "mining engineer",
        # - Mahaut (17..-18.. ; lithographe). Lithographe
        " ; lithographe": "lithographer",
        ". Lithographe": "lithographer",
        # - L'Illustration (Éditeur). Éditeur scientifique
        " (Éditeur)": "editor",
        ". Éditeur scientifique": "editor",
        # - La Pierre, Augustin Denis Édouard (lieutenant de vaisseau)
        " (lieutenant de vaisseau)": "first lieutenant",
    }

    # Rules and matched examples for David Rumsey Map Collection:
    rules_david_rumsey_map_collection = {
        # - Aspioti-ELKA (Firm)
        "(Firm)": "firm",
        # - Thomas, Joseph, publisher
        ", publisher": "publisher",
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
    occupation = None
    for d in rules:
        if d not in name:
            continue
        name = name.replace(d, "")
        occupation = rules[d]
        break

    return name, occupation


def get_name2author(
    processed_metadata: List[ProcessedMetadataEntry],
) -> Dict[str, Author]:
    name_strs = []
    for d in processed_metadata:
        if d["authors"] is None:
            continue
        name_strs += d["authors"]
    name_strs = [*set(name_strs)]

    name2author = {}
    for name_str in name_strs:
        name = replace_substrings(name_str)
        name, occupation = split_occupation(name)
        name, lifespan = split_lifespan(name)
        name2author[name_str] = {
            "name": name.strip(),
            "birth": lifespan["birth"],
            "death": lifespan["death"],
            "occupation": occupation,
            "input": name_str,
        }
    return name2author


def build_authors(processed_metadata: List[ProcessedMetadataEntry]) -> List[Author]:
    name2author = get_name2author(processed_metadata)
    authors = [*name2author.values()]
    authors = sorted(authors, key=lambda d: d["name"] + d["input"])
    return authors
