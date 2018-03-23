#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/index.py" method="post">
        <input type="text" name="name" placeholder="Votre nom" />

        <input type="submit" name="send" value="Envoyer information au serveur" />
    </form>
    <script type="text/javascript">
        function loadJSON(callback) {
            var xobj = new XMLHttpRequest();
                xobj.overrideMimeType("application/json");
            xobj.open('GET', 'playlists.json', true); // Replace 'my_data' with the path to your file
            xobj.onreadystatechange = function () {
                  if (xobj.readyState == 4 && xobj.status == "200") {
                    // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
                    callback(xobj.responseText);
                  }
            };
            xobj.send(null);
        }
        console.log('tight');
        // Call to function with anonymous callback
        loadJSON(function(response) {
            // Do Something with the response e.g.
            //jsonresponse = JSON.parse(response);
            console.log(jsonresponse);
            // Assuming json data is wrapped in square brackets as Drew suggests
            //console.log(jsonresponse[0].name);

        });
    </script>
</body>
</html>
"""

print(html)