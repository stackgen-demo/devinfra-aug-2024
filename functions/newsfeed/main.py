import feedparser

def lambda_handler(event, context):
    feed_url = 'https://lwkd.info/feed.xml'
    
    feed = feedparser.parse(feed_url)
    
    html_content = """
    <html>
    <head>
        <title>{}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
                background-color: #f4f4f4;
            }}
            h1 {{
                color: #333;
                text-align: center;
                border-bottom: 2px solid #333;
                padding-bottom: 10px;
                margin-bottom: 20px;
            }}
            h2 {{
                color: #0056b3;
                margin-top: 30px;
            }}
            a {{
                text-decoration: none;
                color: #0056b3;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            p {{
                margin: 10px 0;
            }}
            .content {{
                padding: 15px;
                background: #fff;
                border: 1px solid #ddd;
                box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }}
            hr {{
                border: 0;
                border-top: 1px solid #eee;
                margin: 40px 0;
            }}
        </style>
    </head>
    <body>
    """.format(feed.feed.title)
    
    html_content += f"<h1>{feed.feed.title}</h1>"
    
    for entry in feed.entries:
        html_content += "<div class='content'>"
        html_content += f"<h2><a href='{entry.link}'>{entry.title}</a></h2>"
        html_content += f"<p><em>Published: {entry.published}</em></p>"
        html_content += f"<p>{entry.summary}</p>"
        html_content += entry.get('content', [{'value': entry.summary}])[0]['value']
        html_content += "</div>"
        html_content += "<hr>"
    
    html_content += "</body></html>"
    
    return {
        'statusCode': 200,
        'body': html_content,
        'headers': {
            'Content-Type': 'text/html'
        }
    }
