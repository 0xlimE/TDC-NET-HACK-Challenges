# CARWEBAPP
Man you tried to mess with this fucking challenge, the solution is __CRAZY__

https://github.com/kramadugu/CARWEBAPP/

The challenge is on the above github, we clone it down and start looking at it.

I just simply tried to run the entrypoint app.py, but I got like a million python3 dependency problems, tons of libraries I didn't have. So the process is.

1. Run `app.py`
2. See that you are missing `python3 dependency X`
3. pip3 install that dependency (god bless you if you are not in a virtual environment)
4. Go back to 1 until it runs smoothly.

In the end this was the dependencies I needed.

```
beautifulsoup4==4.10.0
blis==0.7.6
breadability==0.1.20
catalogue==2.0.7
certifi==2021.10.8
chardet==4.0.0
charset-normalizer==2.0.12
click==8.0.4
cycler==0.11.0
cymem==2.0.6
distro==1.7.0
docopt==0.6.2
Flask==2.0.3
fonttools==4.31.1
gensim==4.1.2
idna==3.3
itsdangerous==2.1.1
Jinja2==3.0.3
joblib==1.1.0
kiwisolver==1.4.0
langcodes==3.3.0
lxml==4.8.0
MarkupSafe==2.1.1
matplotlib==3.5.1
murmurhash==1.0.6
nltk==3.7
numpy==1.22.3
packaging==21.3
pandas==1.4.1
pathy==0.6.1
pikepdf==5.1.0
Pillow==9.0.1
preshed==3.0.6
pycountry==22.3.5
pydantic==1.8.2
pyparsing==3.0.7
python-dateutil==2.8.2
pytz==2022.1
regex==2022.3.15
requests==2.27.1
scipy==1.8.0
six==1.16.0
smart-open==5.2.1
soupsieve==2.3.1
spacy==3.2.3
spacy-legacy==3.0.9
spacy-loggers==1.0.1
srsly==2.4.2
sumy==0.9.0
tabula-py==2.3.0
thinc==8.0.15
tqdm==4.63.0
typer==0.4.0
typing-extensions==4.1.1
urllib3==1.26.9
wasabi==0.9.0
Werkzeug==2.0.3
``` 
THis was of course from pip3 freeze and I did not have to install all these dependencies.

I did all this in a docker-container, the ultimate virtual environment. And finally it runs:

RUN.PNG HERE

Ok we have it up and running and it works

CARWEBAPP HERE

its a crazy huge app with many pages that just straight up doesnt work, so let us look at the source of app.py. Its filled with crazy code, but there is a specific function that should spring to mind.

Namely `render_template_string()`

This is a dangerous function if we can make our user input flow to it, it seems that for many endpoints of the app, there is a possibility of making our input get into the function, but the problem is that most functions look like this

```python3
@app.route('/tableindex',methods=['GET','POST'])
def tblindex():
    if request.method == 'GET':
        page = create_tagger_page(ttags)
        with open('templates/ttag.html',mode='w') as f:
            f.write(page)
        if os.path.exists('templates/ttag.html'):
            return render_template('ttag.html')
    if request.method == 'POST':
        if 'home' in list(request.form.keys()):
            return redirect(url_for('get_submit'))
        site = list(request.form.values())[0]
        df = ttags[site]
        page = None
        with open('templates/ttag.html','r') as f:
            page = f.read()
        page = page.replace('<!-- This is a comment -->',df.to_html())
        
        return render_template_string(page)
```

slightly super freaking hard to decode. 

Since this is a clone2pwn, I only have to show 1 solution, and the solution that I found may not be the simplest, but man get ready for this:

The function that I found you could get user input to flow into `render_template_string()` was the `toc()`function which looks like the following:

```python3
@app.route('/toc',methods=['GET','POST'])
def TOC():
    if request.method == 'GET':
        return render_template_string(tagger_html)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'home' in list(request.form.keys()):
            return redirect(url_for('get_submit'))
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file_tabulas(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            tocs = get_TOC(os.path.join(app.config['UPLOAD_FOLDER'], filename))[0]
            rpage = tagger_html.replace('<!-- This is a comment -->',tocs.to_html(index=False))
            return render_template_string(rpage)
```

Okay lets decipher.

The first four lines just check if the function is a GET or a POST, I know from the source that the variable `tagger_html` cannot contain our user input, so we have to work with the `POST` request.

Ok so the three first `if` statements simply check that we are uploading a valid file, there is not anything to do here. The fun, or simply just wacky stuff starts at the fourth `if` statement.

The `allowed_file_tabulas` function looks like the following:
```
def allowed_file_tabulas(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_TAB
```
with `ALLOWED_EXTENSIONS_TAB` as: 
```
ALLOWED_EXTENSIONS_TAB = {'pdf'}
```

super complicated code to check if the file is a fucking pdf, anyway we need to upload a pdf, and from the name of the function and the html page it looks like we are trying to do something with a ".pdf table of contents"

The next line with the function `secure_filename()` also has some obscure function to make a filename secure, its not worth going into, since the filename is not reflected in the output function.

