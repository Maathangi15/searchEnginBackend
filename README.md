curl -X PUT "localhost:9200/hit_tamil_songs?pretty" -H "Content-Type: application/json" -d @mapping_file.json

curl -X POST "localhost:9200/hit_tamil_songs/_bulk?pretty" -H "Content-Type: application/json" --data-binary @180071P_Mini_Project_Corpus.json
