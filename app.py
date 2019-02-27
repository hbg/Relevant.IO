from flask import Flask, render_template, request
import twitter, json, config
import datetime
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", name="Home")


@app.route('/search')
def fetch():
    unformatted_query = request.args.get('q')
    #   query = "q="+str(request.args.get('q'))+"%20&result_type=popular"
    info = {
        "items": [],
        "urls": [],
        "names": []
    }
    api = config.API
    since, count = "", 25
    if request.args.get('since') is not None:
        #  query += "&since=" + request.args.get('since')
        since = request.args.get('since')
    else:
        year_ago = datetime.datetime.now() - datetime.timedelta(days=3*365)
        #  query += "&since=" + str(year_ago.strftime("%Y-%m-%d"))
        since = str(year_ago.strftime("%Y-%m-%d"))
    if request.args.get('count') is not None:
        #  query += "&count=" + str(request.args.get('count'))
        count = int(request.args.get('count'))
    location = str(request.args.get("loc")).split(",")
    search = api.GetSearch(
        term=str(request.args.get('q')),
        geocode=(location[0], location[1], "50mi"),
        since=since,
        count=count,
        result_type="mixed"
    )  # Replace happy with your search
    for tweet in search:
        #   print(tweet)
        # Low to high interactivity... Twitter already sorted out, but now it's time to add Facebook & Snapchat
        info["items"].append(tweet.text)
        t = json.loads(str(tweet))
        try:
            info["urls"].append(t['urls'][0]["expanded_url"])
            #   print(t['urls'][0]["expanded_url"])
        except:
            info["urls"].append("#")
            #   print("Not found")
        info["names"].append(t['user']['name'])
    return render_template("results.html", name="Results", query=unformatted_query, items=info["items"], urls=info["urls"], names=info["names"])


if __name__ == '__main__':
    app.run(debug=True)
