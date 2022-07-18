import justpy as jp
import Api
import documentation
import defintion

jp.Route("/api",Api.Api.server)
jp.Route("/",documentation.About.serve)
jp.justpy(port=8003)