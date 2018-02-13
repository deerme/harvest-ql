import moz_sql_parser, json, urllib2, sys
from lxml import etree


query_parts = moz_sql_parser.parse("select * from '{\"parser\":\"web-table\",\"url\":\"http://www.gobiernotransparentechile.gob.cl/directorio/entidad/1/1/per_planta/Ao-2017\"}' where table_id = 1 ")

datasets = []

# TODO: implement the lang parser xD

if query_parts['from']:
    uri = json.loads(query_parts['from']['value']['literal'])

    if uri["parser"] == "web-table" :
        print "parser web-table"

        headers = { 'User-Agent' : 'Mozilla/5.0' }
        data = ""
        rq = urllib2.Request( uri["url"] , data, headers)
        rs = urllib2.urlopen(rq)
        raw = rs.read()
        #print raw
        table_id = 1
        for table in etree.HTML(raw).xpath("//table"):
            print "table ", table_id 
            table_data = {"id":"","class":"","table_id" : table_id}
            for property_key in table.attrib:
                table_data[property_key] = table.attrib[property_key] 
      
            rows = table.xpath(".//tr")
            table_data["row_count"] = len(rows)
            
            row_id = 1
            for row in rows:
                row_data = {"row_id" : row_id}
                columns = row.xpath(".//td")
                row_data["column_count"] = len(columns)

                column_id = 1
                for column in columns:
                    row_data[ str("c" + str(column_id))] = ''.join(column.itertext())
                    column_id = column_id +1

                    
                
                datasets_row = {}
                datasets_row.update(table_data)
                datasets_row.update(row_data)
                datasets.append(datasets_row)
                row_id = row_id + 1            
            
            table_id = table_id + 1


        print datasets

        if query_parts['from']:
            # TODO: implement the condition parser
            # {"and": [{"eq": ["table_id", 1]}, {"or": [{"eq": ["column_count", 15]}, {"eq": [1, 1]}]}]}
            # {"and": [{"eq": ["table_id", 1]}, {"eq": ["column_count", 15]}]}
            # {"eq": ["table_id", 1]}
            print 1


print json.dumps( query_parts )


