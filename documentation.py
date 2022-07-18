import justpy as jp

class About:
    path="/about"

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp,classes = "bg-blue-300 h-screen")

        jp.H1(a=div,text="Instant Dictionary App",classes="text-4xl m-2")
        jp.Div(a=div,text="Get definition of Words using our api",classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div,text="www.example.com/api?w=moon")
        jp.Hr(a=div)
        jp.Div(a=div,text ="""
        
        
        
        """)