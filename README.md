# Project2

## Perpose and Design
We hope to realize Sudoku, an interesting game in this project. I hope people who play our games can find happiness and sense of achievement in our games. We have register, login, logout, upload game, personal game records and rank functions in our Sukoku
game. 
In this game, only administrator can upload the game. Default administrator is "admin" and the password is "123456". When admin enter in
the game page, there is a upload button. Admin can upload the new game by input each number in each table, like a real Sudoku game, or,
admin can input a string with numbers separated by ','.
There is some string for testing.
"8,1,7,6,5,9,4,2,3,6,5,3,4,2,8,7,1,9,4,2,9,3,1,7,6,8,5,7,8,2,5,4,6,9,3,1,3,6,5,7,9,1,8,4,2,9,4,1,2,8,3,5,6,7,2,9,6,1,7,4,3,5,8,1,3,8,9,6,5,2,7,4,5,7,4,8,3,2,1,9,6"
The string has a total of 81 digits, and each of the nine digits is a row in the game for a total of nine rows.
## Architecture
```
.
├── forms.py
├── __init__.py
├── models.py
├── __pycache__
│   ├── forms.cpython-38.pyc
│   ├── __init__.cpython-38.pyc
│   ├── models.cpython-38.pyc
│   └── routes.cpython-38.pyc
├── routes.py
├── static
│   ├── avatar120220519144314.jpg
│   ├── avatar120220519144403.jpg
│   ├── avatar320220519023147.jpg
│   ├── bg2.jpg
│   ├── bg.png
│   ├── css
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.css.map
│   │   ├── game.css
│   │   ├── index.css
│   │   ├── introduction.css
│   │   ├── login.css
│   │   ├── personal.css
│   │   └── style.css
│   ├── default_head_pic.jpg
│   ├── js
│   │   ├── bootstrap.min.js
│   │   ├── game.js
│   │   ├── jquery-3.6.0.js
│   │   ├── jquery.js
│   │   ├── personal.js
│   │   └── upload.js
│   ├── sudoku1.jpg
│   └── sudoku.png
└── templates
    ├── base.html
    ├── game.html
    ├── index.html
    ├── introduction.html
    ├── login.html
    ├── personal.html
    ├── rank.html
    ├── register.html
    └── upload.html

5 directories, 39 files
```
We have the static directory, the templates directory, the __init__.py, the forms.py, the models.py and the routes.py.
In the static, there are Javascript code files, CSS code files and some picture sources.
In the templates, there are nine HTML files as templates for flask. And the init.py is used to initial the application. 
The forms.py is used to declare the form submission. The models.py is used to declare the structure of the database. 
Finally, the routes.py is the views file that is backend API of the flask project.

## Prerequisites
Requires python3, flask, venv, and sqlite
### install python3
`sudo apt install python3`

### install python virtual environment
`sudo apt-get install python-virtualenv`

### install pip
`sudo apt install python3-pip`

### install flask
`pip install Flask`

### install sqlite
`sudo apt-get install sqlite3`

## Getting Started
Clone the project from the github: `git clone git@github.com:Changhao029/Project2.git`

Enter the project directory: `cd cd Project2`

Create the python virtual environment: `python3 -m venv venv`

Activate the python virtual enviroment: `source ./venv/bin/activate`

Install all the requirements from the requirements.txt file: `pip install -r requirements.txt`

Initial the database: 

(For test we have uploaded a database file 'project2.db', so if you just want to run the project, you could skip this init to 'flask run')

`flask db init`

`flask db migrate -m "init"`

`flask db upgrade`

To run the app: `flask run`.

To stop the app: Use 'ctrl+ C'.

To exit the environment: `deactivate`

## Running the tests

### 1.Unit test
You will see three Flask instance named "app" in the `./app/__init__.py`, like:
```
app.config.from_object(Config)
# app.config.from_object(Test_Config)
# app.config.from_object(Test_Config_Unit)
```
You should change the code to this:

```
# app.config.from_object(Config)
# app.config.from_object(Test_Config)
app.config.from_object(Test_Config_Unit)
```
And run `python -m unittest testApp.py` in the project root directory. You will see:
```
..<WrapperTestResponse 95 bytes [200 OK]>
............
----------------------------------------------------------------------
Ran 14 tests in 4.399s

OK

```
If you want to see the coverage, you should run:`coverage report ./app/*.py`. You will see:
```
Name                Stmts   Miss  Cover
---------------------------------------
./app/__init__.py      47      5    89%
./app/forms.py         11      0   100%
./app/models.py        33      5    85%
./app/routes.py       243     34    86%
---------------------------------------
TOTAL                 334     44    87%

```

### 2.System test
set the code of `./app/__init__.py` like that
```
# app.config.from_object(Config)
app.config.from_object(Test_Config_Unit)
```
then run `python3 -m tests.systemtest` in the project root directory to run the selenium test, the result will show:
```
----------------------------------------------------------------------
Ran 1 test in 8.002s

OK
```
Then change the code of `./app/__init__.py` to:
```
app.config.from_object(Config)
# app.config.from_object(Test_Config_Unit)
```
and then run the app again.
## Contribution
We each contributed about 50% to the project.
### Changhao Liu contribution review
My partner and I are jointly responsible for the topic selection, design,  development and testing of this project. In the development stage, I was mainly responsible for the back-end code development of login registration and personal page, as well as the front-end code development of the game interface. In addition, my partner and I were responsible for the debugging and testing of the code together. In the testing step, I was mainly responsible for the unit test.

### Yinuo Zhao contribution review
I am mainly responsible for the front-end development of index, base, introduction, login, registration and personal page, as well as the back-end development of game uploading. Both of us participate in selecting topics, designing, debugging and testing the project. I mainly do the system test with selenium.

### github commit log
```
commit 121f5f20785389244cdafefa52538c6ccece9b83
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 23 00:47:09 2022 +0800

    add test db

commit 729776219da904eacbab7420c3167a1809e802dd
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 23 00:42:39 2022 +0800

    add test db

commit cee0da8dc701b1dddbe92ec331d91ff6c7ea10e8
Merge: 151639e 784c20b
Author: Yino <526319623@qq.com>
Date:   Mon May 23 00:40:18 2022 +0800

    Merge branch 'main' of github.com:Changhao029/Project2 into main

commit 151639e47071e96f8a3b36e000449c6234a98531
Author: Yino <526319623@qq.com>
Date:   Mon May 23 00:39:55 2022 +0800

    debug for html

commit 784c20bb76948d73a889ce12581d3801b9f205cc
Author: liu <22924454@student.uwa.edu.au>
Date:   Sun May 22 01:13:37 2022 +0800

    add timer backend

commit 44d0811c57784d3545e69944f5e02d251c27f8f7
Author: Yino <526319623@qq.com>
Date:   Sun May 22 01:01:54 2022 +0800

    add second timer to game.html

commit 861d091a6462d0d6f704de4aedf9c4661626137d
Merge: 60a65e5 1c4ddbc
Author: Yino <526319623@qq.com>
Date:   Sun May 22 00:17:18 2022 +0800

    Merge branch 'main' of github.com:Changhao029/Project2 into main

commit 60a65e5c76452c53c689f5f7169fcf5724773b95
Author: Yino <526319623@qq.com>
Date:   Sun May 22 00:16:57 2022 +0800

    delete unused parameter and modify the page title

commit 1c4ddbc718e208849443cb9fd32ca4a9eb2e9540
Author: liu <22924454@student.uwa.edu.au>
Date:   Fri May 20 01:01:27 2022 +0800

    comment for models

commit e78b2068436033b0849840651becd4b0e251b8b4
Author: liu <22924454@student.uwa.edu.au>
Date:   Fri May 20 00:52:48 2022 +0800

    comment for view functions

commit b5f5bad3eaf59596ae9233b3e223de07300cb14a
Author: Yino <526319623@qq.com>
Date:   Fri May 20 00:49:47 2022 +0800

    complete comments for js

commit 987abb01d62d32d5298807f70e2b6ffa43652987
Author: Yino <526319623@qq.com>
Date:   Fri May 20 00:45:09 2022 +0800

    complete comments

commit 3d12f0235bb210d2c6f755c9d7b9aba9508e566c
Author: liu <22924454@student.uwa.edu.au>
Date:   Fri May 20 00:08:52 2022 +0800

    fix small problems

commit f0dd0ed46a6fc4e29b52be4fcf6b320cf057e3f2
Author: Yino <526319623@qq.com>
Date:   Thu May 19 23:57:46 2022 +0800

    Finish README and solve some little problems

commit 1796a916f6d12cc4fbc990f40103a781276288ab
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 19:55:20 2022 +0800

    readme

commit eab1266718d6f62c06417676839a6fc220f62d16
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 19:54:15 2022 +0800

    readme

commit 6a0b4e44b45df05ae44a62770b9a80288d41e264
Merge: 769cd90 33d4937
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 19:54:07 2022 +0800

    Merge branch 'main' of github.com:Changhao029/Project2 into main

commit 33d4937ce83b22b9c7d75334487b079d9272d4f4
Author: Yino <526319623@qq.com>
Date:   Thu May 19 19:47:11 2022 +0800

    solve the version conflict of selenium's find_element_by_id() function in systemtest

commit 769cd9091292939958630486aa66a5cc24452f71
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 19:42:35 2022 +0800

    readme

commit c56fa5ea1eb8f4aff306f4c869d70c1812c492c3
Author: Yino <526319623@qq.com>
Date:   Thu May 19 19:30:02 2022 +0800

    debug systemtest

commit 2e7b3d97b6d4ce19e79af72d97bafa59d3599940
Merge: f40d7fb 25d4ee2
Author: Yino <526319623@qq.com>
Date:   Thu May 19 19:10:44 2022 +0800

    Merge remote-tracking branch 'origin/main' into main

commit f40d7fb21d9f979edf76631b0fef10a88d832aee
Author: Yino <526319623@qq.com>
Date:   Thu May 19 19:08:19 2022 +0800

    commit geckodriver

commit 25d4ee2cdade0e724cbe361cada297d7fa791325
Author: Yino <526319623@qq.com>
Date:   Thu May 19 19:06:43 2022 +0800

    debug test

commit f02d0037d5aa53dd1339e1deff55da393272b215
Merge: 904ee80 a06cf04
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 17:34:57 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 904ee80b198b6c49b9529df9caa7e7062548b896
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 17:34:05 2022 +0800

    readme and the git log

commit a06cf047ea4dae24f3d9eacddc4ec49782f8cd2d
Author: Yino <526319623@qq.com>
Date:   Thu May 19 15:28:34 2022 +0800

    css validation

commit e27a2c10a21e888a57f331b46ab82f6350dfef02
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 15:25:40 2022 +0800

    add requirements.txt

commit f741a8d37677642d9afb804c49ca15bf89c7e698
Merge: 0e8d530 44840d4
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 15:23:05 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 44840d43114ce0c6740fae58001c19d73db4cac7
Author: Yino <526319623@qq.com>
Date:   Thu May 19 15:22:29 2022 +0800

    html validation

commit 0e8d530b037deb03d7306c778347a1853ca6124f
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 15:15:38 2022 +0800

    change result color

commit 5c62104ec13f8ba7135d65edac33559dabf0add3
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 15:00:54 2022 +0800

    validation html pages and add unitest part

commit 078bb8d9d3339461431d84b8ed389f4ffdd3c2bf
Author: Yino <526319623@qq.com>
Date:   Thu May 19 14:27:31 2022 +0800

    debug for templates

commit 93d649cc9f4376072ab99d0a6ecfc828767fbf3b
Author: Yino <526319623@qq.com>
Date:   Thu May 19 14:19:54 2022 +0800

    debug for templates

commit d271e831546d06906d7b36f0e8533a804bbf7239
Author: Yino <526319623@qq.com>
Date:   Thu May 19 12:22:17 2022 +0800

    modify test config

commit ecfe4651984d3518faaaf2489b7a229c9cdd9fe5
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 10:22:38 2022 +0800

    change game every day

commit 89e07f4a0f9958e5577cb4074e10f374eb6e195c
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 02:30:14 2022 +0800

    change __init__.py

commit b5f88b65bc20ca11bd5a24e1fe35735b2205e436
Merge: c1b30df e12f590
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 02:26:21 2022 +0800

    unitest

commit e12f59074fb9ba9595770b7818edea830ce1be1b
Author: Yino <526319623@qq.com>
Date:   Thu May 19 02:21:40 2022 +0800

    change api

commit c1b30dfae1b2475a9e609b4f105127f22a391fc6
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 19 02:06:35 2022 +0800

    unitest

commit 7005407030503ba691649e7487b802362cb51b32
Author: Yino <526319623@qq.com>
Date:   Thu May 19 02:05:20 2022 +0800

    Debug systemtest.py

commit 458ca00442f65560f596e9b4a034b6cb114fdf3d
Author: Yino <526319623@qq.com>
Date:   Thu May 19 01:33:36 2022 +0800

    develop systemtest with selenium

commit 52cb86568d3e0bbe1b86108865a970929f06f85a
Author: Yino <526319623@qq.com>
Date:   Thu May 19 01:32:48 2022 +0800

    develop systemtest with selenium

commit 286d1f2ff25a3dca9386ffcc8fb9e1c9302193c3
Author: Yino <526319623@qq.com>
Date:   Wed May 18 19:53:03 2022 +0800

    debug personal.html

commit b86ee32d336acd9b5874173d3b7b7e4b7157a845
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 17:30:38 2022 +0800

    add pagination in personal page

commit 65d1764cbaad1e95930728ed6b0cdd5dd5ea92a1
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 16:33:56 2022 +0800

    after win the game lock the table and delete the button

commit 08c446deb84ff7b36a5397bdf99fe70f77042199
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 16:10:57 2022 +0800

    improve upload validation

commit 572b647d34da579b9a4705aec239adfce072a8a1
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 15:13:59 2022 +0800

    upload validation

commit 02794971316d8233c0a38feb6f34865d22411f45
Author: Yino <526319623@qq.com>
Date:   Wed May 18 14:15:43 2022 +0800

    add introduction.css

commit 42f0c7af82a1b0d9f5ce911b9c5ff6b1a0599e67
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 12:19:21 2022 +0800

    fix bugs

commit bb4a0b75dcf741b2f2f949b2860b6c49c058a299
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 11:48:10 2022 +0800

    rollback the code

commit 74bdac4d5a9e0933dc0e6d05a288d411fd504830
Merge: 09a4247 26dbc23
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 11:47:18 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 26dbc2310ae4e1066a1ab135291fc0e1cb52672a
Author: Yino <526319623@qq.com>
Date:   Wed May 18 11:43:21 2022 +0800

    complete personal.html

commit 09a4247e0b795bd6cee4567bb327e6fc9019be67
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 09:40:51 2022 +0800

    stay logged in

commit 3a03866eb97ce0fc6d7a7aaae34352c91970d6e5
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 01:11:24 2022 +0800

    change the rank list

commit 1261b31649a1bb64e642b4f4651d9546d66c767d
Merge: 7a59194 efafac2
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 18 00:50:30 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit efafac224f20fcf40e40cadfea33d11396b8930d
Merge: ab3e64d a8289f1
Author: Yino <526319623@qq.com>
Date:   Wed May 18 00:48:12 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

     Conflicts:
    	app/routes.py
    	app/templates/personal.html

commit ab3e64d127ad5b35f56265cd63c9b6ed4a8a555b
Author: Yino <526319623@qq.com>
Date:   Wed May 18 00:45:08 2022 +0800

    develop personal.html and complete pop-up window

commit 7a59194f8f546e68850f761b412fefc9b0256eb1
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 17 23:18:02 2022 +0800

    change the input verification

commit a8289f1b9b041bd073cbd035f5f0e22bb8cff545
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 17 22:01:38 2022 +0800

    change the personal page

commit e98cbe1d05384935b83c50917a42f1883acb28f1
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 17 21:53:31 2022 +0800

    change the rank list

commit 6e388b026442127e6519a4268bcd840d7dad1750
Author: Yino <526319623@qq.com>
Date:   Tue May 17 21:42:18 2022 +0800

    develop upload function to support upload in string

commit b54019a407abecf6fc5969225ba228d1930ad32f
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 17 18:12:48 2022 +0800

    change start time and the finish time

commit 3af0afd66a364a5bfafe7f04a03b16b4b1d33f3d
Author: Yino <526319623@qq.com>
Date:   Tue May 17 18:03:43 2022 +0800

    develop introduction.html

commit 8125d0506e8074f0467703115160fdd634282c07
Author: Yino <526319623@qq.com>
Date:   Tue May 17 16:28:05 2022 +0800

    debug 'is_admin'

commit b401a52c7189a2e2370b4938731e89a219672a47
Author: Yino <526319623@qq.com>
Date:   Tue May 17 16:24:27 2022 +0800

    develop introduction

commit a03a0210f7e10919a0cd557a52e3e1931a0f2998
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 17 16:13:37 2022 +0800

    improve avatar function

commit a690df48ef47b791f42a54bfd227f7d453c7a02a
Merge: 5e41a97 745ec40
Author: Yino <526319623@qq.com>
Date:   Tue May 17 15:17:01 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 5e41a9715ee12d30fe5a18fa9e58448a1d67c4f3
Author: Yino <526319623@qq.com>
Date:   Tue May 17 15:10:33 2022 +0800

    complete index and develop introduction

commit 745ec400bcb42c4123b385f8258f710c0491f83a
Merge: 5a8479c f16391c
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 17 12:22:06 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 5a8479c5e5a7b2f61c5760faa00251c2efa1c789
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 17 12:21:45 2022 +0800

    add avatar function

commit f16391c296b91824c45dde5b4ce3010f751ad64a
Merge: 116f45e b3f50f3
Author: Yino <526319623@qq.com>
Date:   Tue May 17 01:03:10 2022 +0800

    Merge remote-tracking branch 'origin/dev' into dev

commit 116f45e193c51bb8da38e6b26177582ab99b1344
Author: Yino <526319623@qq.com>
Date:   Tue May 17 01:02:00 2022 +0800

    index page development

commit b3f50f3a47eafdc42206e948860a8bcb82134cd2
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 22:50:01 2022 +0800

    fix base.html bug

commit 3a3b3cae7100aaecf8a56e8f93a3fdee9ca962b4
Merge: f4fa433 47c5032
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 22:47:52 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 47c5032998d6673c4696e8eab57c95a740faeb5a
Author: Yino <526319623@qq.com>
Date:   Mon May 16 22:45:11 2022 +0800

    index page development

commit f4fa4335dc5a37508bc0a3f5220edde0eb7a8e25
Merge: fdd92ac 9213baa
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 22:34:20 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

     Conflicts:
    	app/static/js/upload.js

commit 9213baa956dd98cb09e03ca53924c6065679df75
Author: Yino <526319623@qq.com>
Date:   Mon May 16 22:33:57 2022 +0800

    upload.js

commit fdd92ac63177b438f32e77ccf724391560907059
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 22:24:06 2022 +0800

    fix bugs in game view

commit f684ffe0eb83f31e31b6dbb12ef0191ac48c3755
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 20:55:45 2022 +0800

    link upload in the game page when the gamer is an admin

commit e0fef665c15fdf4c3542c6882fc6809a33d101c2
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 20:21:58 2022 +0800

    add MD5 to password in register step

commit 9727443ece36a6faa60dcde55f969712504c0adf
Merge: 225ac91 fc3c10e
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 20:08:29 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 225ac9166f940ec7d345c8c5e6925f2585241be2
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 16 20:07:37 2022 +0800

    add personal page

commit fc3c10e40f76ad442cb016117377f1e4289c8aa1
Author: Yino <526319623@qq.com>
Date:   Wed May 11 23:44:47 2022 +0800

    Add REST API

commit e7fb389eaf25e3cce14ef0de1bb62b706fd13701
Author: liu <22924454@student.uwa.edu.au>
Date:   Wed May 11 00:09:49 2022 +0800

    add rank function in the game page, and add default admin in the initial step, and change user table

commit 6eaad5dabd9a9a76e103cff4da7860cd4fbb71c6
Author: Yino <526319623@qq.com>
Date:   Tue May 10 23:15:59 2022 +0800

    develop game upload function and upload.html

commit 9f710bd6453d365912a4550c7f73436934c4cb11
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 10 20:24:07 2022 +0800

    no user login and start game

commit 70ddec283442a7e7928ed231ba216eea05cb7563
Merge: 3c8ad32 7cb4588
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 10 13:08:07 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

commit 7cb458845e194d675936d31a0317b062adab52af
Author: Yino <526319623@qq.com>
Date:   Tue May 10 13:07:49 2022 +0800

    add "remember me" function to login.html; modify the game.css and login.css

commit 3c8ad32680bf85b24d3b3c15075d1c835c539430
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 10 13:03:07 2022 +0800

    index page frontend

commit 5af7313f1617d61a9408e86eb8ed1a0c89757356
Author: liu <22924454@student.uwa.edu.au>
Date:   Tue May 10 11:25:02 2022 +0800

    add some pictures

commit 94173cec174b3e881a3f08bbbc55b7ea28e048cc
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 9 23:26:33 2022 +0800

    change index.html, and improve login and register views

commit 94dcb9399d96059db86c05fc31869654c1fb5095
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 9 17:46:13 2022 +0800

    random space in the game table

commit e7fd278cce667fbfc70a365f7cce3ef490e98f8d
Merge: 68b3a2b a0637c4
Author: Yino <526319623@qq.com>
Date:   Mon May 9 17:00:16 2022 +0800

    Merge branch 'dev' of github.com:Changhao029/Project2 into dev

     Conflicts:
    	app/templates/game.html

commit 68b3a2bbbfa3229f9196d695a353c6c51aa7f42f
Author: Yino <526319623@qq.com>
Date:   Mon May 9 16:57:33 2022 +0800

    develop index.html and game.html

commit a0637c46df456e502acba1fcf267e249f5c7ca86
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 9 15:26:36 2022 +0800

    add result in db

commit 425df020564c3a18735ae0ba8b110d143481cf27
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 9 09:37:42 2022 +0800

    move game css code to static folder

commit 95d432ff91d404f669a0a3b92e89d65435f1405c
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 9 09:20:32 2022 +0800

    improve the static folder structure

commit 1bed0e62326494634b79f7f8402811b6be6e1beb
Author: liu <22924454@student.uwa.edu.au>
Date:   Mon May 9 09:09:04 2022 +0800

    add start button

commit a3788f1802101c4e61bcf400567cd81bd0ec08c2
Author: liu <22924454@student.uwa.edu.au>
Date:   Sun May 8 23:11:15 2022 +0800

    game table loading

commit 78effd84bcab73700189eadcacb462982b1ff3d3
Author: Yino <526319623@qq.com>
Date:   Sun May 8 22:18:56 2022 +0800

    design login.html and register.html

commit 06ca761c910133cdb949d1e520cd41ad904244b2
Merge: 4d6a33e 7e776bd
Author: Yino <526319623@qq.com>
Date:   Sun May 8 19:44:22 2022 +0800

    Merge remote-tracking branch 'origin/dev' into dev

commit 4d6a33ec3daca8fb6835c7c5f5fd7a8f53fa14f5
Author: Yino <526319623@qq.com>
Date:   Sun May 8 19:44:08 2022 +0800

    add static files and design base.html, game.html

commit 7e776bd37f58d59b817f741ef16b4d96436e65e1
Author: liu <22924454@student.uwa.edu.au>
Date:   Sun May 8 15:41:32 2022 +0800

    game rank and sort

commit be3123f111add17d6098109aebc55dd33cad2e7b
Author: Yino <526319623@qq.com>
Date:   Sun May 8 15:22:36 2022 +0800

    create game table

commit e0ed63d9dc3aacc7f5b54e7077e4ee9817b59597
Author: Yino <526319623@qq.com>
Date:   Sat May 7 23:21:04 2022 +0800

    delete the db file

commit e50e9a789dd6d119a05d34ad1c41915e232fd466
Author: Yino <526319623@qq.com>
Date:   Sat May 7 23:08:01 2022 +0800

    develop base.html navigation bar

commit 7827469a37c98edb2eda4e09a832bd8f1fb6b2ca
Author: Yino <526319623@qq.com>
Date:   Sat May 7 23:06:10 2022 +0800

    develop base.html navigation bar

commit 1935be3d9337a2436472c39079f29ee60cc792b6
Author: liu <22924454@student.uwa.edu.au>
Date:   Sat May 7 15:31:30 2022 +0800

    change gitignore

commit 5025113519d74fd1aac16c9f6f2b3c99e9adda07
Author: liu <22924454@student.uwa.edu.au>
Date:   Sat May 7 15:28:45 2022 +0800

    get current user information, and change the login.html and the register.html

commit fa0de75fc8301d26a2de7d9b01cc363d7e71e466
Author: Yino <526319623@qq.com>
Date:   Thu May 5 22:58:01 2022 +0800

    login function modify

commit 0754c390032850d3618267207356dd4d66566e0d
Author: Yino <526319623@qq.com>
Date:   Thu May 5 21:51:36 2022 +0800

    login function

commit e353e4a7afcef8749760c161764503ec415e69c1
Merge: 713204e 21bb925
Author: Yino <526319623@qq.com>
Date:   Thu May 5 19:58:46 2022 +0800

    Merge remote-tracking branch 'origin/dev' into dev

    # Conflicts:
    #       project2.db

commit 713204eeb9f8d57aea65235625e1e18723818050
Author: Yino <526319623@qq.com>
Date:   Thu May 5 19:58:13 2022 +0800

    add user to test

commit 21bb9251050719fba2f6550dc7c4443845594008
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 5 19:56:52 2022 +0800

    can not input the username that are in the DB

commit fda3c3c9a1b371884c12e7ba339d3418c92bc0a6
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 5 19:15:09 2022 +0800

    register back-end code

commit ad32376ef964095ac0a514af0cfc77aa930b9683
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 5 18:51:31 2022 +0800

    merge the code with Yinuo

commit e481569a27285922f3fb4338eab19bd4aea084ab
Author: Yino <526319623@qq.com>
Date:   Thu May 5 17:12:39 2022 +0800

    develop login function

commit 29c52decae65a516fa602b6cff9b14f90b83c9df
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 5 16:59:11 2022 +0800

    create a user table, and develop register.html

commit 61c84ab612b857780b4e2b748899e41b104af5c7
Author: liu <22924454@student.uwa.edu.au>
Date:   Thu May 5 11:07:17 2022 +0800

    Print "Hello, world" to test the project.

commit 638be011ba1c6d5369595c0505172a455336c1d0
Author: Yino <526319623@qq.com>
Date:   Thu May 5 10:29:40 2022 +0800

    Initial the flask app

commit 95c3241cf12a8931287eb476db5a47beff4d2dfd
Author: Changhao029 <104755987+Changhao029@users.noreply.github.com>
Date:   Thu May 5 09:59:26 2022 +0800

    Initial commit


```

