import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
KSV = 'd341d4f5b0'
SECRET_KEY = 'a46b8248e515e 859c89cd3b7e44 cbdc4d253e3b84 6bbc15fedfa843 \
				bde70ae61a28a1 262a6955ae6796 776053270c0795 5b0d928a36fc18 \
				871b1c12856640 99b35afd88f022 0a25a8044885f8 cac301c1a7bff9 \
				cffb562bd61324 e259771e79e817 ade1c44e422f36 4b04032284d0a0 \
				3887c6f9b28dd1 c91586dd0d5c3d 57f98807b499d4 6eb80ef6b21bc6 \
				7dd01d28ab915d 01ab3b3513be2a e2c48529129d67 7e59dead1b99d4 \
				dab23f7ae630ec 61039b51b287ab 71ef820601330c 6c27641d29dcab \
				39f71bc96f3624 fad39f6803de5b 570d4dabcccf7c c28fb5712d2907 \
				a10c3437e69e6 cc6e8d3401fa6f 776f141fee69f4 0b491f13bf3988 \
				1e4de88d9cef6a a43afd9edc4c4e 19e0d859cdf1b0 7f654065a5a356'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

