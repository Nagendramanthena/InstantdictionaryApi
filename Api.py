import justpy as jp
import defintion

class Api:

    @classmethod
    def server(cls,req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        definiton_for_word = defintion.Definition(word).getdefiniton()
        wp.html = definiton_for_word
        return wp

jp.Route("/api",Api.server)
jp.justpy()