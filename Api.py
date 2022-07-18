import justpy as jp
import defintion
import json

class Api:

    @classmethod
    def server(cls,req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        definiton_for_word = defintion.Definition(word).getdefiniton()

        response = {
            "word":word,
            "definition":definiton_for_word,
            "example":"www.example.com/api?word=moon"
        }
        wp.html = json.dumps(response)
        return wp

jp.Route("/api",Api.server)
jp.justpy()