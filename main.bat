@Echo off
chcp 65001

wmic /USER:{FAMILY}\{USER} /PASSWORD:{PASSWORD} /NODE:"{NODE}" /OUTPUT:"{DIRECTORY}{NODE}_product.csv" product get name,version,description,installdate,installlocation /FORMAT:CSV
wmic /USER:{FAMILY}\{USER} /PASSWORD:{PASSWORD} /NODE:"{NODE}" /OUTPUT:"{DIRECTORY}{NODE}_logicaldisk.csv" logicaldisk where drivetype=3 get freespace,deviceid,size /FORMAT:CSV
systeminfo /S {NODE} /U {FAMILY}\{USER} /P {PASSWORD} /fo csv > {DIRECTORY}{NODE}_systeminfo.csv
