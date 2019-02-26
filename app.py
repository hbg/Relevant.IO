from flask import Flask, render_template, request
import twitter, json, config
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", name="Home")
@app.route('/search')
def fetch():
    query = str(request.args.get('q'))
    info={
        "items" : [],
        "urls" : [],
        "names" : []
    }
    api = twitter.Api(
            consumer_key=config.consumer_key,
            consumer_secret=config.consumer_secret,
            access_token_key=config.access_token_key,
            access_token_secret=config.access_token_secret
    )
    search = api.GetSearch(
    raw_query="q="+query+"%20&result_type=recent&since=2014-07-19&count=100"
    ) # Replace happy with your search
    for tweet in search:
        info["items"].append(tweet.text)
        t = json.loads(str(tweet))
        try:
            info["urls"].append(t['urls'][0]["expanded_url"])
            print(t['urls'][0]["expanded_url"])
        except:
            info["urls"].append("")
            print("Not found")
        info["names"].append(t['user']['name'])
    return render_template("results.html", name="Results", query=query, items=info["items"], urls=info["urls"], names=info["names"])

if __name__ == '__main__':
    app.run(debug=True)
