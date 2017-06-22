"""
> show dbs
admin   0.000GB
local   0.000GB
testdb  0.135GB
> use testdb
switched to db testdb
> db.artist.find({'area':'Japan'});
{ "_id" : ObjectId("594aa127a0780309cc3f7f5c"), "id" : 723554, "tags" : [ { "count" : 1, "value" : "hello project related" } ], "name" : "Priest", "area" : "Japan", "gid" : "6b45a7c4-e2f8-49ff-af57-b5829b4ed8bb", "sort_name" : "Priest", "type" : "Group", "ended" : true }
{ "_id" : ObjectId("594aa127a0780309cc3f81a3"), "id" : 883036, "ended" : true, "gender" : "Male", "area" : "Japan", "gid" : "b62558bc-3753-46ba-9c62-793bd3d76251", "sort_name" : "Ōnuki, Kazunori", "type" : "Person", "name" : "大貫和紀", "begin" : { "month" : 3, "year" : 1965, "date" : 12 } }
{ "_id" : ObjectId("594aa127a0780309cc3f81fe"), "id" : 883037, "ended" : true, "gender" : "Male", "area" : "Japan", "gid" : "9c6870f8-c226-4727-bada-50d6360424d5", "sort_name" : "Fukutomi, Masayuki", "type" : "Person", "name" : "福富雅之", "begin" : { "month" : 12, "year" : 1978, "date" : 13 } }
{ "_id" : ObjectId("594aa127a0780309cc3f828d"), "id" : 883038, "ended" : true, "gender" : "Female", "area" : "Japan", "gid" : "660ced8e-94ab-4375-883c-861766887e9a", "sort_name" : "YORI", "type" : "Person", "name" : "YORI" }
{ "_id" : ObjectId("594aa127a0780309cc3f83ab"), "id" : 886719, "ended" : true, "gender" : "Male", "area" : "Japan", "gid" : "d1db47e5-f1d0-4493-96c8-d61c88a194fc", "sort_name" : "Aoyama, Mio", "type" : "Person", "name" : "Mio Aoyama", "begin" : { "month" : 7, "year" : 1974, "date" : 24 } }
{ "_id" : ObjectId("594aa127a0780309cc3f8400"), "id" : 851609, "ended" : true, "gender" : "Female", "area" : "Japan", "gid" : "1c0d0f50-2fb9-4064-b701-1408b09c66f7", "sort_name" : "Aoki, Ume", "type" : "Person", "name" : "蒼樹うめ" }
{ "_id" : ObjectId("594aa127a0780309cc3f848e"), "id" : 62728, "tags" : [ { "count" : 1, "value" : "likedis auto" } ], "name" : "CURIO", "area" : "Japan", "gid" : "ac97005c-a43b-44ea-afef-19c18a04f808", "sort_name" : "CURIO", "type" : "Group", "ended" : true }
{ "_id" : ObjectId("594aa127a0780309cc3f8537"), "aliases" : [ { "sort_name" : "Frankfurt/Tokyo Connection", "name" : "Frankfurt/Tokyo Connection" } ], "id" : 208977, "ended" : true, "gender" : "Male", "area" : "Japan", "gid" : "c8ce647c-0573-406f-8ce0-a2c59e8a198c", "sort_name" : "Frankfurt-Tokio-Connection", "type" : "Person", "name" : "Frankfurt-Tokio-Connection" }
{ "_id" : ObjectId("594aa127a0780309cc3f8566"), "aliases" : [ { "sort_name" : "Kurata Masayo", "name" : "Kurata Masayo" }, { "sort_name" : "くらた まさよ", "name" : "くらた まさよ" }, { "sort_name" : "倉田 雅世", "name" : "倉田 雅世" }, { "sort_name" : "くらたまさよ", "name" : "くらたまさよ" } ], "tags" : [ { "count" : 1, "value" : "jazz and blues" }, { "count" : 1, "value" : "artist-cv" } ], "name" : "倉田雅世", "begin" : { "month" : 5, "year" : 1969, "date" : 21 }, "id" : 151379, "ended" : true, "gender" : "Female", "area" : "Japan", "gid" : "96045be3-6f31-4cb2-a838-0ec332f1f9f4", "sort_name" : "Kurata, Masayo", "type" : "Person" }
{ "_id" : ObjectId("594aa127a0780309cc3f8577"), "id" : 628530, "ended" : true, "gender" : "Male", "area" : "Japan", "gid" : "9e505e10-90d5-45e7-8de6-7ea5d37c3148", "sort_name" : "Koike, Takahiro", "type" : "Person", "name" : "古池孝浩" }
{ "_id" : ObjectId("594aa127a0780309cc3f864c"), "id" : 632495, "tags" : [ { "count" : 1, "value" : "ひだまりスケッチ" }, { "count" : 1, "value" : "character" } ], "gender" : "Female", "ended" : true, "area" : "Japan", "gid" : "7c82a2e3-5f86-4109-8602-7b2a11cdc487", "sort_name" : "Yoshinoya-sensei", "type" : "Character", "name" : "吉野屋先生" }
{ "_id" : ObjectId("594aa127a0780309cc3f86d8"), "id" : 800984, "ended" : true, "gender" : "Male", "area" : "Japan", "gid" : "29fc2b70-aace-43df-a7b7-75d97d15d62c", "sort_name" : "Ikuhara, Kunihiko", "type" : "Person", "name" : "幾原邦彦", "begin" : { "month" : 12, "year" : 1964, "date" : 21 } }
{ "_id" : ObjectId("594aa127a0780309cc3f87be"), "aliases" : [ { "sort_name" : "朝日 祭", "name" : "朝日 祭" } ], "id" : 850533, "ended" : true, "gender" : "Female", "area" : "Japan", "gid" : "80827b55-5c4c-4455-b4d5-0dc89e54aa06", "sort_name" : "Asahisai", "type" : "Person", "name" : "朝日祭", "begin" : { "month" : 12, "date" : 25 } }
{ "_id" : ObjectId("594aa127a0780309cc3f88d1"), "id" : 932003, "ended" : true, "gender" : "Male", "area" : "Japan", "gid" : "8ad6c2ff-151e-431d-85a3-b4fdaa4d247f", "sort_name" : "Iwasa, Toshihide", "type" : "Person", "name" : "岩佐俊秀", "begin" : { "month" : 11, "year" : 1975, "date" : 18 } }
{ "_id" : ObjectId("594aa127a0780309cc3f896e"), "id" : 249135, "ended" : true, "area" : "Japan", "gid" : "98a5eaaa-7f6a-43ec-88cd-3d54250c2e68", "sort_name" : "S-Word", "name" : "S-Word" }
{ "_id" : ObjectId("594aa127a0780309cc3f897a"), "id" : 1095761, "tags" : [ { "count" : 1, "value" : "likedis auto" } ], "ended" : true, "area" : "Japan", "gid" : "3c2783bb-8548-44f3-96cd-9a2fa80fbf39", "sort_name" : "Especia", "type" : "Group", "name" : "Especia", "begin" : { "month" : 6, "year" : 2012, "date" : 1 } }
{ "_id" : ObjectId("594aa127a0780309cc3f89a4"), "id" : 883058, "ended" : true, "gender" : "Female", "area" : "Japan", "gid" : "69dabc45-f487-488c-9d4a-092100d2d205", "sort_name" : "Hattori, Makiko", "type" : "Person", "name" : "服部マキコ" }
{ "_id" : ObjectId("594aa127a0780309cc3f8b09"), "aliases" : [ { "sort_name" : "雅 智弥", "name" : "雅 智弥" } ], "id" : 848667, "ended" : true, "area" : "Japan", "gid" : "c50d6435-deec-4b0a-8eb7-59a603a5b608", "sort_name" : "雅智弥", "type" : "Person", "name" : "雅智弥" }
{ "_id" : ObjectId("594aa127a0780309cc3f8b87"), "id" : 848668, "ended" : true, "area" : "Japan", "gid" : "687bc200-dac3-49ff-9555-a44a849a0b1c", "sort_name" : "I.N", "name" : "I.N" }
{ "_id" : ObjectId("594aa127a0780309cc3f8ebd"), "id" : 848673, "ended" : true, "area" : "Japan", "gid" : "bdc31fa9-d91c-49b5-ae50-a502858e1e50", "sort_name" : "小間浩子", "type" : "Person", "name" : "小間浩子" }
Type "it" for more
> db.artist.find({'area':'Japan'});.count()
2017-06-22T03:27:25.246+0900 E QUERY    [thread1] SyntaxError: expected expression, got '.' @(shell):1:33
> db.artist.find({'area':'Japan'}).count()
22821

"""
