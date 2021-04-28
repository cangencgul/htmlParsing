from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (f"Start : {tag}")
        self.printAttrs(attrs)
    def handle_endtag(self, tag):
        print (f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print (f"Empty : {tag}")
        self.printAttrs(attrs)
    def printAttrs(self, attrs):
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

        
if __name__ == '__main__':
    lines = ""
    for i in range(int(input())):
        lines += input()
    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()
    parser.feed(lines)
