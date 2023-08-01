# Alabama Maps

This directory stores data obtained from [Alabama Maps Historical Map Archive](http://alabamamaps.ua.edu/historicalmaps/).

For more information about this data source, see the [data source documentation](https://oldvis.github.io/libquery_extensions/api/alabama-maps.html).

## Search Result

- [Alabama Maps Historical Map Archive](http://alabamamaps.ua.edu/historicalmaps/) categorizes images into 6 themes
    - ALABAMA
    - THE UNITED STATES AND CANADA
    - THE WORLD
    - WESTERN HEMISPHERE
    - EASTERN HEMISPHERE
    - SPECIAL TOPICS
- After briefly browsing the web pages, we observe that only the theme SPECIAL TOPICS contains visualization images.
- SPECIAL TOPICS contains 17 sub-themes
    - American Revolution
    - Biblical and The Holy Land
    - American Civil War
    - Coastal Navigation Charts
    - Coastal Topographic Sheets (T-Sheets)
    - Geologic Atlas of the United States
    - Lighthouses
    - Mississippi River
    - Mexican American War
    - National Forests
    - Native Americans
    - Railroads
    - U.S.D.A. Prime Farmland Maps
    - U.S.D.A. Soil Survey Maps
    - World War I
    - World War II - Pacific Theater
    - World War II - News Maps
- We browsed each of the sub-themes and found that the following 6 sub-themes had similar web page structures. Thus, we focused on fetching data from these 6 sub-themes. 
    - [Native Americans](http://alabamamaps.ua.edu/historicalmaps/nativeamericans/index.html)
    - [American Revolution](http://alabamamaps.ua.edu/historicalmaps/american_revolution/index.html)
    - [Biblical](http://alabamamaps.ua.edu/historicalmaps/Biblical/Index.htm)
    - [Mississippi River](http://alabamamaps.ua.edu/historicalmaps/MississippiRiver/index.html)
    - [Mexican American War](http://alabamamaps.ua.edu/historicalmaps/mexican-americanwar/index.html)
    - [World War I](http://alabamamaps.ua.edu/historicalmaps/worldwarI/index.html)
    - [American Civil War](http://alabamamaps.ua.edu/historicalmaps/civilwar/index.html)
        - Generalized Maps
            - [Virginia & the Seat of War](http://alabamamaps.ua.edu/historicalmaps/civilwar/gen-seatofwar.html)
            - [Western Theater](http://alabamamaps.ua.edu/historicalmaps/civilwar/gen-westerntheater.html)
            - [Georgia & the Southeast](http://alabamamaps.ua.edu/historicalmaps/civilwar/gen-gasoutheast.html)
            - [Routes of Union Activity in Alabama](http://alabamamaps.ua.edu/historicalmaps/civilwar/unionroutes.html)
        - Battles
            - [Atlanta](http://alabamamaps.ua.edu/historicalmaps/civilwar/atlanta.html)
            - [Antietam/Sharpsburg](http://alabamamaps.ua.edu/historicalmaps/civilwar/antietam.html)
            - [Bull Run/Manassas](http://alabamamaps.ua.edu/historicalmaps/civilwar/bullrun.html)
            - [Chattanooga](http://alabamamaps.ua.edu/historicalmaps/civilwar/chattanooga.html)
            - [Chickamauga](http://alabamamaps.ua.edu/historicalmaps/civilwar/chickamauga.html)
            - [Franklin](http://alabamamaps.ua.edu/historicalmaps/civilwar/franklin.html)
            - [Fredericksburg](http://alabamamaps.ua.edu/historicalmaps/civilwar/fredericksburg.html)
            - [Gettysburg](http://alabamamaps.ua.edu/historicalmaps/civilwar/gettysburg.html)
            - [Harrisburg, Mississippi](http://alabamamaps.ua.edu/historicalmaps/civilwar/harrisburg.html)
            - [Murfreesboro](http://alabamamaps.ua.edu/historicalmaps/civilwar/murfreesboro.html)
            - [New Market](http://alabamamaps.ua.edu/historicalmaps/civilwar/NewMarket.html)
            - [Second Bull Run](http://alabamamaps.ua.edu/historicalmaps/civilwar/secondbullrun.html)
            - [Seven Pines](http://alabamamaps.ua.edu/historicalmaps/civilwar/sevenpines.html)
            - [Shiloh](http://alabamamaps.ua.edu/historicalmaps/civilwar/shiloh.html)
            - [Vicksburg](http://alabamamaps.ua.edu/historicalmaps/civilwar/vicksburg.html)
- After a brief look at the other 10 sub-themes, we found few instances of typical visualizations. Moreover, as these pages are different structures, it is hard to efficiently fetch data from them. Thus, we currently ignore these themes in the data fetching progress.
    - [Coastal Navigation Charts](http://alabamamaps.ua.edu/historicalmaps/navigationcharts/index.html) (~180 images)
        - This sub-theme contains maps with nautical isobath ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Navigation%20Charts/NavStPaulHarbor_AK.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=default/view.xsl&plugin=true)). They are edge cases of visualizations.
    - [Coastal Topographic Sheets](http://alabamamaps.ua.edu/historicalmaps/Coastal%20Survey%20Maps/index.html) (~150 images)
        - This sub-theme contains general geographic maps ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Coastal%20Topography%20Sheets%20(T-maps)/T1042.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=default/view.xsl&plugin=true)) and maps with isolines ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Coastal%20Topography%20Sheets%20(T-maps)/T-1508.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=default/view.xsl&plugin=true)).
    - [Geologic Atlas of the United States](http://alabamamaps.ua.edu/historicalmaps/Geologic%20Atlas%20Folios/index1.html) (~900 images)
        - This sub-theme contains maps with isolines ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=USGS%20Geologic%20Atlas%20Folios/Montana%20Livingston%201893%20topography.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=simple/view-dhtml.xsl)). Some of them use colors to represent categories.
    - [Lighthouses](http://alabamamaps.ua.edu/historicalmaps/Lighthouses/LighthouseIndex.html) (~180 images)
        - This sub-theme contains general geographic maps ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Lighthouses/Lighthouse1898a.sid&wid=1000&hei=900&props=item(Name,Description),cat(Name,Description)&style=simple/view-dhtml.xsl)).
    - [National Forests](http://alabamamaps.ua.edu/historicalmaps/nationalforests/indexmap.htm) (~120 images)
        - This sub-theme contains maps with color encoding ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=National%20Forests/Alabama/Alabama%20NF%20all%20forests%201965.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=simple/view-dhtml.xsl)).
    - [Railroads](http://alabamamaps.ua.edu/historicalmaps/railroads/index.html) (56 images)
        - This sub-theme contains geographic maps with railroads ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Railroads/Railroad1869a.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=simple/view-dhtml.xsl)).
    - [U.S.D.A. Prime Farmland Maps](http://alabamamaps.ua.edu/historicalmaps/primefarmland/index.html) (~100 images)
        - This sub-theme contains maps with color encoding ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Prime%20Farmland/Arizona/Maricopa%20Sheet%207.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=default/view.xsl&plugin=true)).
    - [U.S.D.A. Soil Survey Maps](http://alabamamaps.ua.edu/historicalmaps/soilsurvey/index.html) (~100 images)
        - This sub-theme contains maps with color encoding ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Soil%20Surveys/West%20Virginia/West%20Virginia%20Monroe%201925.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=default/view.xsl&plugin=true)). Some maps also use density encoding ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=Soil%20Surveys/Alabama/Autauga%20County%20AL%201908.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=default/view.xsl&plugin=true)).
    - [World War II - Pacific Theater](http://alabamamaps.ua.edu/historicalmaps/World%20War%20II/World%20War%20II%20Pacific.htm) (433 images)
        - This sub-theme contains thematic maps ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=World%20War%20II/Pacific/Australia/WW2%20Pacific%20Australia%20Australia.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=simple/view-dhtml.xsl)).
    - [World War II - News Maps](http://alabamamaps.ua.edu/historicalmaps/World%20War%20II/WW2%20Newsmaps.htm) (178 images)
        - This sub-theme contains maps with textual annotations ([example](http://cartweb.geography.ua.edu/lizardtech/iserv/calcrgn?cat=Special%20Topics&item=World%20War%20II/News%20Maps/Vol%203%20No%2044%202-19-45.sid&wid=500&hei=400&props=item(Name,Description),cat(Name,Description)&style=simple/view-dhtml.xsl)).

## Image Types

The visualizations in this data source are mainly thematic maps that with color encoding or glyphs.
