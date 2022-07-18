import justpy as jp
import defintion
import json

class Api:

    @classmethod
    def server(cls,req):
        wp = jp.WebPage()
        word = req.query_params.get('word')
        definiton_for_word = defintion.Definition(word).getdefiniton()
        if definiton_for_word:

            response = {
            "word":word,
            "definition":definiton_for_word,
            "example":"www.example.com/api?word=moon"
            }

            wp.html = json.dumps(response)

        else:
            reponse={
                "word": word,
                "definition": "definiton for word not found sorry :(",
                "example": "www.example.com/api?word=moon"
            }

            wp.html = json.dumps(reponse)
        return wp

