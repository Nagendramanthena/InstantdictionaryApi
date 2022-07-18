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
        {"word": "moon", "definition": ["A natural satellite of a planet.", "A month, particularly a lunar month (approximately 28 days).", "To fuss over adoringly or with great affection.", "Deliberately show ones bare ass (usually to an audience, or at a place, where this is not expected or deemed appropriate).", "To be lost in phantasies or be carried away by some internal vision, having temorarily lost (part of) contact to reality."], "example": "www.example.com/api?word=moon"}
        
        
        """)

        return wp