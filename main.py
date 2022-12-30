from website import create_app
from webbrowser import open as openWebsite

openWebsite("http://127.0.0.1:6969")
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=6969, threaded=True)

"""    <script defer src="{{ url_for('static', filename='theme.js') }}"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}" />"""