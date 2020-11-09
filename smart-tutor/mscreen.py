from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.theming import ThemeManager
from kivymd.uix.picker import MDDatePicker, MDThemePicker
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
import pymysql
from kivy.core.window import Window
import webbrowser as wb

Window.size = (400, 600)


class MenuScreen(Screen):
    pass


class RegisterScreen(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                dbname = 'test'
                dbhost = 'localhost'
                dbpass = ''
                dbuser = 'root'
                db = pymysql.connect(dbhost, dbuser, dbpass, dbname)
                print("Database connected successfully.")
                cur = db.cursor()
                cur.execute("select Email from smart where Email= %s", self.email.text)
                usercheck = cur.fetchone()
                # loadpass =
                cur2 = db.cursor()
                cur2.execute("select Password from smart where Password = %s", self.password.text)
                passcheck = cur2.fetchone()
                #print(usercheck)

                if usercheck == None:
                    print('New user')
                    sql = '''
                    INSERT INTO smart(Name,Email,Password) values(%s, %s, %s)
                    '''
                    val = (self.namee.text, self.email.text, self.password.text)
                    try:

                        cur.execute(sql, val)
                        db.commit()
                        self.newuser()
                        print('Data inserted successfully.')



                    except:
                        db.rollback()

                        db.close()
                elif self.email.text == usercheck[-1]:
                    print('user already exsist')
                    self.userexsist()
                self.reset()
                sm.current = "login"

            else:
                invalidForm()
        else:
            invalidForm()

    def userexsist(self):
        pop = Popup(title='sorry',
                    content=Label(text='User already exsist.'),
                    size_hint=(None, None), size=(200, 100))

        pop.open()

    def newuser(self):
        pop = Popup(title='congrats',
                    content=Label(text='Registered successfully.'),
                    size_hint=(None, None), size=(200, 100))
        pop.open()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


def invalidForm():
    pop = Popup(title='Invalid Form',
                content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 100))

    pop.open()


def invalidForm1():
    pop = Popup(title='Invalid Form',
                content=Label(text='Email exists already'),
                size_hint=(None, None), size=(400, 100))

    pop.open()


class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_btn(self):
        dbname = 'test'
        dbhost = 'localhost'
        dbpass = ''
        dbuser = 'root'
        db = pymysql.connect(dbhost, dbuser, dbpass, dbname)
        print("Database connected successfully.")
        cur = db.cursor()
        cur.execute("select Email from smart where Email= %s", self.email.text)
        usercheck = cur.fetchone()
        cur2 = db.cursor()
        cur2.execute("select Password from smart where Password = %s", self.password.text)
        passcheck = cur2.fetchone()
        u = usercheck[-1]
        print(u)
        p = ''.join(passcheck)

        if self.email.text == u and self.password.text == p:
            on_press: root.manager.current = 'home'
            print('pass')
            self.reset()

        db.commit()
        db.close()

    def reset(self):
        self.email.text = ""
        self.password.text = ""

    def invalidForm():
        pop = Popup(title='Invalid Form',
                    content=Label(text='Please fill in all inputs with valid information.'),
                    size_hint=(None, None), size=(400, 100))
        pop.open()


class HomeScreen(Screen):
    pass


class HigherSecondary(Screen):
    pass


class Assessment(Screen):
    pass


class Secondary(Screen):
    pass


class Primary(Screen):
    pass


class KinderGarden(Screen):
    pass


class Pkg(Screen):
    pass


class Lkg(Screen):
    pass


class Ukg(Screen):
    pass


class First(Screen):
    pass


class Second(Screen):
    pass


class Third(Screen):
    pass


class Fourth(Screen):
    pass


class Fifth(Screen):
    pass


class Sixth(Screen):
    pass


class Seventh(Screen):
    pass


class Eighth(Screen):
    pass


class Ninth(Screen):
    pass


class Tenth(Screen):
    pass


class Eleventh(Screen):
    pass


class Twelve(Screen):
    pass


class Prekgenglishsub(Screen):
    pass


class Prekgtamilsub(Screen):
    pass


class Prekgmathssub(Screen):
    pass


class Prekgsciencesub(Screen):
    pass


class Lkgenglishsub(Screen):
    pass


class Lkgtamilsub(Screen):
    pass


class Lkgmathssub(Screen):
    pass


class Lkgsciencesub(Screen):
    pass


class Ukgenglishsub(Screen):
    pass


class Ukgtamilsub(Screen):
    pass


class Ukgmathssub(Screen):
    pass


class Ukgsciencesub(Screen):
    pass


class Firstenglishsub(Screen):
    pass


class Firsttamilsub(Screen):
    pass


class Firstmathssub(Screen):
    pass


class Firstsciencesub(Screen):
    pass


class Secondenglishsub(Screen):
    pass


class Secondtamilsub(Screen):
    pass


class Secondmathssub(Screen):
    pass


class Secondsciencesub(Screen):
    pass


class Thirdenglishsub(Screen):
    pass


class Thirdtamilsub(Screen):
    pass


class Thirdmathssub(Screen):
    pass


class Thirdsciencesub(Screen):
    pass


class Thirdsocialsciencesub(Screen):
    pass


class Fourthenglishsub(Screen):
    pass


class Fourthtamilsub(Screen):
    pass


class Fourthmathssub(Screen):
    pass


class Fourthsciencesub(Screen):
    pass


class Fourthsocialsciencesub(Screen):
    pass


class Fifthenglishsub(Screen):
    pass


class Fifthtamilsub(Screen):
    pass


class Fifthmathssub(Screen):
    pass


class Fifthsciencesub(Screen):
    pass


class Fifthsocialsciencesub(Screen):
    pass


class Sixthenglishsub(Screen):
    pass


class Sixthtamilsub(Screen):
    pass


class Sixthmathssub(Screen):
    pass


class Sixthsciencesub(Screen):
    pass


class Sixthsocialsciencesub(Screen):
    pass


class Seventhenglishsub(Screen):
    pass


class Seventhtamilsub(Screen):
    pass


class Seventhmathssub(Screen):
    pass


class Seventhsciencesub(Screen):
    pass


class Seventhsocialsciencesub(Screen):
    pass


class Eightthenglishsub(Screen):
    pass


class Eightthtamilsub(Screen):
    pass


class Eightthmathssub(Screen):
    pass


class Eightthsciencesub(Screen):
    pass


class Eightthsocialsciencesub(Screen):
    pass


class Ninethenglishsub(Screen):
    pass


class Ninethtamilsub(Screen):
    pass


class Ninethmathssub(Screen):
    pass


class Ninethsciencesub(Screen):
    pass


class Ninethsocialsciencesub(Screen):
    pass


class Tenthenglishsub(Screen):
    pass


class Tenthtamilsub(Screen):
    pass


class Tenthmathssub(Screen):
    pass


class Tenthsciencesub(Screen):
    pass


class Tenthsocialsciencesub(Screen):
    pass


class Eleventhenglishsub(Screen):
    pass


class Eleventhchemistrysub(Screen):
    pass


class Eleventhmathssub(Screen):
    pass


class Eleventhphysicssub(Screen):
    pass


class Eleventhbiologysub(Screen):
    pass


class Twelthenglishsub(Screen):
    pass


class Twelthchemistrysub(Screen):
    pass


class Twelthmathssub(Screen):
    pass


class Twelthphysicssub(Screen):
    pass


class Twelthbiologysub(Screen):
    pass


class Prekgenglishmaterials(Screen):
    pass


class Prekgtamilmaterials(Screen):
    pass


class Prekgmathsmaterials(Screen):
    pass


class Prekgsciencematerials(Screen):
    pass


class Prekgsocialsciencematerials(Screen):
    pass


class Lkgenglishmaterials(Screen):
    pass


class Lkgtamilmaterials(Screen):
    pass


class Lkgmathsmaterials(Screen):
    pass


class Lkgsciencematerials(Screen):
    pass


class Lkgsocialsciencematerials(Screen):
    pass


class Ukgenglishmaterials(Screen):
    pass


class Ukgtamilmaterials(Screen):
    pass


class Ukgmathsmaterials(Screen):
    pass


class Ukgsciencematerials(Screen):
    pass


class Ukgsocialsciencematerials(Screen):
    pass


class Firstenglishmaterials(Screen):
    pass


class Firsttamilmaterials(Screen):
    pass


class Firstmathsmaterials(Screen):
    pass


class Firstsciencematerials(Screen):
    pass


class Firstsocialsciencematerials(Screen):
    pass


class Secondenglishmaterials(Screen):
    pass


class Secondtamilmaterials(Screen):
    pass


class Secondmathsmaterials(Screen):
    pass


class Secondsciencematerials(Screen):
    pass


class Secondsocialsciencematerials(Screen):
    pass


class Thirdenglishmaterials(Screen):
    pass


class Thirdtamilmaterials(Screen):
    pass


class Thirdmathsmaterials(Screen):
    pass


class Thirdsciencematerials(Screen):
    pass


class Thirdsocialsciencematerials(Screen):
    pass


class Fourthenglishmaterials(Screen):
    pass


class Fourthtamilmaterials(Screen):
    pass


class Fourthmathsmaterials(Screen):
    pass


class Fourthsciencematerials(Screen):
    pass


class Fourthsocialsciencematerials(Screen):
    pass


class Fifthenglishmaterials(Screen):
    pass


class Fifthtamilmaterials(Screen):
    pass


class Fifthmathsmaterials(Screen):
    pass


class Fifthsciencematerials(Screen):
    pass


class Fifthsocialsciencematerials(Screen):
    pass


class Sixthenglishmaterials(Screen):
    pass


class Sixthtamilmaterials(Screen):
    pass


class Sixthmathsmaterials(Screen):
    pass


class Sixthsciencematerials(Screen):
    pass


class Sixthsocialsciencematerials(Screen):
    pass


class Seventhenglishmaterials(Screen):
    pass


class Seventhtamilmaterials(Screen):
    pass


class Seventhmathsmaterials(Screen):
    pass


class Seventhsciencematerials(Screen):
    pass


class Seventhsocialsciencematerials(Screen):
    pass


class Eightthenglishmaterials(Screen):
    pass


class Eightthtamilmaterials(Screen):
    pass


class Eightthmathsmaterials(Screen):
    pass


class Eightthsciencematerials(Screen):
    pass


class Eightthsocialsciencematerials(Screen):
    pass


class Ninethenglishmaterials(Screen):
    pass


class Ninethtamilmaterials(Screen):
    pass


class Ninethmathsmaterials(Screen):
    pass


class Ninethsciencematerials(Screen):
    pass


class Ninethsocialsciencematerials(Screen):
    pass


class Tenthenglishmaterials(Screen):
    pass


class Tenthtamilmaterials(Screen):
    pass


class Tenthmathsmaterials(Screen):
    pass


class Tenthsciencematerials(Screen):
    pass


class Tenthsocialsciencematerials(Screen):
    pass


class Eleventhenglishmaterials(Screen):
    pass


class Eleventhchemistrymaterials(Screen):
    pass


class Eleventhmathsmaterials(Screen):
    pass


class Eleventhphysicsmaterials(Screen):
    pass


class Eleventhbiologymaterials(Screen):
    pass


class Twelthenglishmaterials(Screen):
    pass


class Twelthchemistrymaterials(Screen):
    pass


class Twelthmathsmaterials(Screen):
    pass


class Twelthphysicsmaterials(Screen):
    pass


class Twelthbiologymaterials(Screen):
    pass


class Prekgenglishvideos(Screen):
    pass


class Prekgtamilvideos(Screen):
    pass


class Prekgmathsvideos(Screen):
    pass


class Prekgsciencevideos(Screen):
    pass


class Prekgsocialsciencevideos(Screen):
    pass


class Lkgenglishvideos(Screen):
    pass


class Lkgtamilvideos(Screen):
    pass


class Lkgmathsvideos(Screen):
    pass


class Lkgsciencevideos(Screen):
    pass


class Lkgsocialsciencevideos(Screen):
    pass


class Ukgenglishvideos(Screen):
    pass


class Ukgtamilvideos(Screen):
    pass


class Ukgmathsvideos(Screen):
    pass


class Ukgsciencevideos(Screen):
    pass


class Ukgsocialsciencevideos(Screen):
    pass


class Firstenglishvideos(Screen):
    pass


class Firsttamilvideos(Screen):
    pass


class Firstmathsvideos(Screen):
    pass


class Firstsciencevideos(Screen):
    pass


class Firstsocialsciencevideos(Screen):
    pass


class Secondenglishvideos(Screen):
    pass


class Secondtamilvideos(Screen):
    pass


class Secondmathsvideos(Screen):
    pass


class Secondsciencevideos(Screen):
    pass


class Secondsocialsciencevideos(Screen):
    pass


class Thirdenglishvideos(Screen):
    pass


class Thirdtamilvideos(Screen):
    pass


class Thirdmathsvideos(Screen):
    pass


class Thirdsciencevideos(Screen):
    pass


class Thirdsocialsciencevideos(Screen):
    pass


class Fourthenglishvideos(Screen):
    pass


class Fourthtamilvideos(Screen):
    pass


class Fourthmathsvideos(Screen):
    pass


class Fourthsciencevideos(Screen):
    pass


class Fourthsocialsciencevideos(Screen):
    pass


class Fifthenglishvideos(Screen):
    pass


class Fifthtamilvideos(Screen):
    pass


class Fifthmathsvideos(Screen):
    pass


class Fifthsciencevideos(Screen):
    pass


class Fifthsocialsciencevideos(Screen):
    pass


class Sixthenglishvideos(Screen):
    pass


class Sixthtamilvideos(Screen):
    pass


class Sixthmathsvideos(Screen):
    pass


class Sixthsciencevideos(Screen):
    pass


class Sixthsocialsciencevideos(Screen):
    pass


class Seventhenglishvideos(Screen):
    pass


class Seventhtamilvideos(Screen):
    pass


class Seventhmathsvideos(Screen):
    pass


class Seventhsciencevideos(Screen):
    pass


class Seventhsocialsciencevideos(Screen):
    pass


class Eightthenglishvideos(Screen):
    pass


class Eightthtamilvideos(Screen):
    pass


class Eightthmathsvideos(Screen):
    pass


class Eightthsciencevideos(Screen):
    pass


class Eightthsocialsciencevideos(Screen):
    pass


class Ninethenglishvideos(Screen):
    pass


class Ninethtamilvideos(Screen):
    pass


class Ninethmathsvideos(Screen):
    pass


class Ninethsciencevideos(Screen):
    pass


class Ninethsocialsciencevideos(Screen):
    pass


class Tenthenglishvideos(Screen):
    pass


class Tenthtamilvideos(Screen):
    pass


class Tenthmathsvideos(Screen):
    pass


class Tenthsciencevideos(Screen):
    pass


class Tenthsocialsciencevideos(Screen):
    pass


class Eleventhenglishvideos(Screen):
    pass


class Eleventhchemistryvideos(Screen):
    pass


class Eleventhmathsvideos(Screen):
    pass


class Eleventhphysicsvideos(Screen):
    pass


class Eleventhbiologyvideos(Screen):
    pass


class Twelthenglishvideos(Screen):
    pass


class Twelthchemistryvideos(Screen):
    pass


class Twelthmathsvideos(Screen):
    pass


class Twelthphysicsvideos(Screen):
    pass


class Twelthbiologyvideos(Screen):
    pass


class Assessments(Screen):
    pass
class Help(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(RegisterScreen(name='reg'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(HigherSecondary(name='hyper'))
sm.add_widget(Secondary(name='sec'))
sm.add_widget(Primary(name='prim'))
sm.add_widget(KinderGarden(name='kg'))
sm.add_widget(Pkg(name='pkg'))
sm.add_widget(Lkg(name='lkg'))
sm.add_widget(Ukg(name='ukg'))
sm.add_widget(First(name='first'))
sm.add_widget(Second(name='second'))
sm.add_widget(Third(name='third'))
sm.add_widget(Fourth(name='fourth'))
sm.add_widget(Fifth(name='fifth'))
sm.add_widget(Sixth(name='sixth'))
sm.add_widget(Seventh(name='seventh'))
sm.add_widget(Eighth(name='eighth'))
sm.add_widget(Ninth(name='ninth'))
sm.add_widget(Tenth(name='tenth'))
sm.add_widget(Eleventh(name='eleventh'))
sm.add_widget(Twelve(name='twelve'))
sm.add_widget(Assessment(name='ass'))
sm.add_widget(Assessments(name='assess'))
sm.add_widget(Help(name='help'))


class SmartTutorApp(MDApp):

    def build(self):
        screen = Builder.load_file('main.kv')

        return screen

    def build1(self):
        return sm

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    # tc1
    def show_prekgtamilmaterialsc1(self):
        wb.open_new(r'https://i.ytimg.com/vi/5qukbSEjmXc/maxresdefault.jpg')

    # ec1
    def show_prekgenglishmaterialsc1(self):
        wb.open_new(
            r'https://i1.wp.com/freepikpsd.com/wp-content/uploads/2017/08/English-Alphabets.png?resize=700%2C467')

    # eg
    def show_prekgenglishmaterialsgif(self):
        wb.open_new(
            r'https://www.bing.com/th/id/OGC.22daa64f18c80eac5d3aaeaddef7385d?pid=1.7&rurl=https%3a%2f%2fmedia.giphy.com%2fmedia%2fuyq3rRQ2Tz31u%2fgiphy.gif&ehk=teqBxIZGuHnbD2uEb2P%2bY%2fLi0khuPTbCptGBkPuGuNo%3d')

    # ew
    def show_prekgenglishmaterialswords(self):
        wb.open_new(r'https://iraparenting.com/wp-content/uploads/2018/10/4-1.jpg')

    # Mn
    def show_prekgmathsmaterialsnumbers(self):
        wb.open_new(r'https://th.bing.com/th/id/OIP.fBRPKz5rCXO2WkMftNpG6QHaEK?w=302&h=180&c=7&o=5&dpr=1.25&pid=1.7')
        # mex1

    def show_prekgmathsmaterialsex1(self):
        wb.open_new(r'https://www.teachstarter.com/wp-content/uploads/2019/02/preview-16946-1170-0-landscape.png')
        # mex2

    def show_prekgmathsmaterialsex2(self):
        wb.open_new(r'https://s-media-cache-ak0.pinimg.com/736x/86/9e/65/869e65858e6b136314fac2dc774255bc.jpg')
        # sf

    def show_prekgsciencematerialsfruits(self):
        wb.open_new(r'https://i.pinimg.com/736x/a0/94/4a/a0944a03514eca5f174d8e21ea2b2022.jpg')
        # sv

    def show_prekgsciencematerialsveg(self):
        wb.open_new(r'https://i.pinimg.com/736x/a0/94/4a/a0944a03514eca5f174d8e21ea2b2022.jpg')

    # tik
    def show_lkgtamilmaterialsume(self):
        wb.open_new(r'https://i.pinimg.com/736x/a0/94/4a/a0944a03514eca5f174d8e21ea2b2022.jpg')

    # tka
    def show_lkgtamilmaterialska(self):
        wb.open_new(r'https://i.pinimg.com/736x/a0/94/4a/a0944a03514eca5f174d8e21ea2b2022.jpg')

    # ewp1
    def show_lkgenglishmaterialswordsp1(self):
        wb.open_new(r'https://i.pinimg.com/736x/a0/94/4a/a0944a03514eca5f174d8e21ea2b2022.jpg')

    # ewp2
    def show_lkgenglishmaterialswordsp2(self):
        wb.open_new(r'https://i.pinimg.com/736x/2b/7f/d3/2b7fd3be8644da674d37fb0ef56197af.jpg')

    # ewp3
    def show_lkgenglishmaterialswordsp3(self):
        wb.open_new(r'https://i.ytimg.com/vi/tJxSr7bZMJg/maxresdefault.jpg')

    # mn100
    def show_lkgmathsmaterialsnumbers100(self):
        wb.open_new(r'https://www.learnerworksheet.com/wp-content/uploads/2019/04/Number-Chart-1-100-1024x699.png')

        # mninw

    def show_lkgmathsmaterialsnumbersinwords(self):
        wb.open_new(
            r'https://www.bing.com/th?id=OIP.XXnHP1gZ-low0-XgTO0qiQHaK7&amp;w=120&amp;h=160&amp;c=8&amp;rs=1&amp;qlt=90&amp;dpr=1.25&amp;pid=3.1&amp;rm=2')

    # sb
    def show_lkgsciencematerialsbirds(self):
        wb.open_new(r'https://i.ytimg.com/vi/r3g3F4AsreQ/maxresdefault.jpg')

    # sa
    def show_lkgsciencematerialsanimals(self):
        wb.open_new(r'http://allpicts.in/wp-content/uploads/2017/06/domestic-animals-with-names.jpg')

    # tl
    def show_ukgtamilmaterialsletters(self):
        wb.open_new(r'https://i.pinimg.com/originals/fc/67/ee/fc67ee16479460c3ff65b845324441a3.jpg')

    # tw
    def show_ukgtamilmaterialswords(self):
        wb.open_new(r'https://i.pinimg.com/originals/3e/81/a7/3e81a70aae18b89e2fbc08bdb76a73c4.png')

    # evc
    def show_ukgenglishmaterialsvowelsandconsonants(self):
        wb.open_new(
            r'https://th.bing.com/th/id/OIP.MvtXy0OgciQ4bSCs4aBBhQHaFU?w=240&amp;h=180&amp;c=7&amp;o=5&amp;dpr=1.25&amp;pid=1.7')

    # ec
    def show_ukgenglishmaterialscolours(self):
        wb.open_new(r'https://s-media-cache-ak0.pinimg.com/736x/22/ac/9b/22ac9b32769915952d978ba75cd27255.jpg')

    # mn1000
    def show_ukgmathsmaterialsnumbers1000(self):
        wb.open_new(
            r'https://41ff701vpzvf2ulz052zsy42-wpengine.netdna-ssl.com/wp-content/uploads/2018/08/1-1000-in-10s-1.jpg')

    # mo
    def show_ukgmathsmaterialsoperations(self):
        wb.open_new(
            r'https://th.bing.com/th/id/OIP.exEe67VbrblSRqxJ_KnkLAHaHa?w=178&amp;h=180&amp;c=7&amp;o=5&amp;dpr=1.25&amp;pid=1.7')

    # ss
    def show_ukgsciencematerialsseasons(self):
        wb.open_new(r'https://i.pinimg.com/originals/69/7b/fb/697bfb9e38050677880e8db0d577a0a4.jpg')

    # sg
    def show_ukgsciencematerialsgoodhabits(self):
        wb.open_new(r'https://i.ytimg.com/vi/taiPUN09uX8/maxresdefault.jpg')

    # tt1
    def show_firsttamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1zkCqiAj5T39LcwDsFd2ulLcyqgkZkpQb')

    # tt2
    def show_firsttamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=16q6XfxnOzvq-NEElBett8zXQo0jHKsBK')

    # tt3
    def show_firsttamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1o5ertuFtc0pMp64WiI5DV3AcUBS6rFzZ')

    # et1
    def show_firstenglishmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=161_oIUtROWU0eFJsOfdNCphD8eC_IAlx')

    # et2
    def show_firstenglishmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1lodJXNuPrjx2QC2C-lEENlzkIoWhQrBk')

    # et3
    def show_firstenglishmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1BsQehRKi9RRg5UZvfjXb28MZA-DaSRsd')

    # mt1
    def show_firstmathsmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1ni1wPgYqS1CBW655YGZa_v---VH7fMY0')

    # mt2
    def show_firstmathsmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1w8QdS2izYEbVTM5fFqMZpY1bKXmiJ-h7')

    # mt3
    def show_firstmathsmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1vsgjI9vdPW4dTNF9l-68YKRM4alfjcnt')

    # st1
    def show_firstsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1Uu0OQfMZhS9BLtXORVBtJLTbLboh19qR')

    # st2
    def show_firstsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1G96AuJR-baUAKAv2UdZ_TUWKun6K1pgC')

    # st3
    def show_firstsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1jcHB90CecAp70RUQa3o7x_35LlmL39UI')

        # tt1

    def show_secondtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1A1VFLvsESnCAiIPLuZu7U3F1XB6ZEfmx')
        # tt2

    def show_secondtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1KCXr5Xt7LL_2kMufaRsX1XLi7--xmmgo')
        # tt3

    def show_secondtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1zGyqvYDPu7fz64GDcDMwim6gKrIRuBB9')

        # et1

    def show_secondenglishmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1xkqfx9HcDCJE8xlbFR3V6hawH26jUtbP')
        # et2

    def show_secondenglishmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1Jph4E9DBtp7QmCFr-0LDz5ZH9LEuYCix')
        # et3

    def show_secondenglishmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1FSLzoiU_o62WrLQJljAWfTGE_0xSPWCW')
        # mt1

    def show_secondmathsmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=12MM1qlav5a10BJJzVF1ga9HGOz2PuSiz')
        # mt2

    def show_secondmathsmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1K0e59qz0yMHny5iI8MFw90C989LSJxON')
        # mt3

    def show_secondmathsmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1hX9v_1y5gt9s3Bnz2Fif1WV6i5gNZu5m')
        # st1

    def show_secondsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1SbXNmfefFui5StC8dM7jDSI-zdLsMW5m')
        # st2

    def show_secondsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1JsMyehjFiIcnC2977xUvYKyeiYZqu6QF')
        # st3

    def show_secondsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=113uaz41mAdHNOoqNSq1EvV9v5Emmyv9v')

    # tt1

    def show_thirdtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1AE_sD05LdZ2tQwBx3g0_49wZnJ9Wj7-5')
        # tt2

    def show_thirdtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1GykZk2OpGxHnqo7Rolx7DdCD3ELU83LZ')
        # tt3

    def show_thirdtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1W4tzvfIpc4nTNdQJ5ERPGDm0PYt1U-OM')

        # et1

    def show_thirdenglishmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1jhD_qlYo-GqGn4yeI_oAFEwve_ue66Nk')
        # et2

    def show_thirdenglishmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1FzKFwmaH3RcPnURjLpqca4EYWyEVZ_UU')
        # et3

    def show_thirdenglishmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1KV7Lu_IAAsIvGoeLca3AIbHpQgbD5CRZ')
        # mt1

    def show_thirdmathsmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1iOwJxHq1l-ghSd-T0Q6v50nXec_OQ2eK')
        # mt2

    def show_thirdmathsmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1fznerChtubCeo_USdIydF9cMZ4mhmZlZ')
        # mt3

    def show_thirdmathsmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1o71ho_T8CtqkuiCnCibr-nHaw-WKwegx')
        # st1

    def show_thirdsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1QZDCWdP2gEWnFy5wFUOAy8cZsiODAVDE')
        # st2

    def show_thirdsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1NRGRnEU6z88OUJvfUkBbbFZADIQTOM3P')
        # st3

    def show_thirdsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1FQMFK9EZHgDVtJ0-KI6lT_I_SezV5txj')

        # st1

    def show_thirdsocialsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1JWwDrb0PvDNr67dz9TeoyfTwjUpSOnw_')
        # st2

    def show_thirdsocialsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1DeUhLF09zRbHpgvwKUiVFxPTIURjMrzt')
        # st3

    def show_thirdsocialsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1dI3pAJqLkiWItWmGUvqJvBDv4UkM-buj')

    def show_fourthtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=10tZX1j2dSq8yEK32qeYypZTaloB6WID9')
        # tt2

    def show_fourthtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1tj6XuGhsUg6aAjtKU8LhyzG8ZSe1YCWd')
        # tt3

    def show_fourthtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1IAp5m17OJdrZdxmeylmu_h_gPhM5JaU7')

        # et1

    def show_fourthenglishmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1Ou39T0SLGzirxhZuOb9qAmdRCs0XQCI0')
        # et2

    def show_fourthenglishmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1_iiwiDvV21hN5AbO4pyj4CRvCuFZgANr')
        # et3

    def show_fourthenglishmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=18QauOQaJXPk9TwLAVf09oDfYV3g2H_-W')
        # mt1

    def show_fourthmathsmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1b_yUmHZ2dhEsJ5SsIQZd9cXw9wK7kd1l')
        # mt2

    def show_fourthmathsmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1IBGc-N0mP1IS7EiEA4fY25J6ECwJdhTO')
        # mt3

    def show_fourthmathsmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=17rvfZQi40BSQJMDW7vKKD3qHkutGgna4')
        # st1

    def show_fourthsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1iDnl3yZqjisbX8T3rUxCFeVrSOF6r_3I')
        # st2

    def show_fourthsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1MjdeeShZ5xCrFjay3MLm_17XNsxvtXgG')
        # st3

    def show_fourthsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=18oaiPE8eM5UGiYQIzb9ysCJQQ5gTXbVu')

        # st1

    def show_fourthsocialsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1Z4vxcI-wgjGiiBBehsBjTcBYb0JVr1bE')
        # st2

    def show_fourthsocialsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1lywEQBl2jNXXMbD0vSTMu_x6rUqWFDBy')
        # st3

    def show_fourthsocialsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1BSpoVNsK8zRORVsj78k-vColHX_SXnG-')

    # tt1
    def show_fifthtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1EVMIzNEdoHs1M3NVsVIBbnOezLjnoY0c')
        # tt2

    def show_fifthtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1LNyWbjc50cuMfT_YFKTVhlToh8MmtuVu')
        # tt3

    def show_fifthtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1ZYR4LJKJ9nZYEuzsIX0v9u2ZG_tYZaXa')

        # et1

    def show_fifthenglishmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1n0RVGiR1I_8qsfR4Qu8AI9PzqJJwJqxr')
        # et2

    def show_fifthenglishmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1LqxOiwh1jt85g4xMfm7oya65ERSnWvck')
        # et3

    def show_fifthenglishmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1Ee--zsqhWwbDHxJw25JZScn4_z7b9ZN6')
        # mt1

    def show_fifthmathsmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1lQZ2Wy0ux-hHOaIp-U6BYN-kckqb5cgM')
        # mt2

    def show_fifthmathsmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1vZjEeK4fM2fICX2I_mTfOWx8u52zgIPy')
        # mt3

    def show_fifthmathsmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=11w5DEi55QK72MfWcEkN-9y6kOaL0Dngr')
        # st1

    def show_fifthsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=10Agtr_mMfgmrVxEjVvEDrhJKKaE2qC4m')
        # st2

    def show_fifthsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1vIkdanUdq2lxm3qm9jLE-Z6GR21oiFnr')
        # st3

    def show_fifthsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1h2Xryj7a61D1YCU9L_18C8sJf8sodDWV')

        # st1

    def show_fifthsocialsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=14zfSJaTYRGAxU9bZsNzFRmOEde8f82O0')
        # st2

    def show_fifthsocialsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1rxHdD-mprhgrMjIiXtS80PvLe6HcI7Fv')
        # st3

    def show_fifthsocialsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=12OM2nZhuztwBcuaKdpiammR5MzF2E0IS')

    # tt1

    def show_sixthtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1Z69ZV4WMcYzQqpQYFGmtgYqfI1gOyBpN')
        # tt2

    def show_sixthtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=10m3doa8gjZ_yymWYF9zhKT8_U6vaGelU')
        # tt3

    def show_sixthtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=12dM0v2yMD3IOIE3qtRmM19HICZbtkVet')

        # et1

    def show_sixthenglishmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1cwzrBz21CSvqYuQ72ysfQrI0E84eqJh6')
        # et2

    def show_sixthenglishmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=15kX2aShVsjvNGJy7QqDcW6PJ0S6juOQL')
        # et3

    def show_sixthenglishmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1UEq2PVlVTuPegUUMKcVR9DDtYXOHDFEK')
        # mt1

    def show_sixthmathsmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1tAG9LcxIdHcq9_5ae77tQY5s9RGvxVCg')
        # mt2

    def show_sixthmathsmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1HC2ij2dsw44tLV_GhrFYv7xhR3d5PKtU')
        # mt3

    def show_sixthmathsmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1fXJy1c3iGxYAhRMebVnyvhjqwJPwRE9i')
        # st1

    def show_sixthsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1AYGdDUST3r1rft3AN__yOxqpUMz84qP5')
        # st2

    def show_sixthsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1n_NYyxuBnzVpthFiEpu1q5bMMFg1gpBO')
        # st3

    def show_sixthsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1gjln8Ca6Foi4E9r32Fj6XmHK1yxsK0V7')

        # st1

    def show_sixthsocialsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=15YtuuXhBiXS9O8pHc55506UsWImh5dkO')
        # st2

    def show_sixthsocialsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1j1JHaQGUxgl717st2dB1g3e5ADL1075n')
        # st3

    def show_sixthsocialsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1GjzdmCSNZGiNEO_PmOAwxEQGPZ8njcBh')

        # tt1

    def show_seventhtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1-lqxyLr3wZY5KrbZmzcOHXk9aAOiLFnq')
        # tt2

    def show_seventhtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1J3fTdO_clDpPraZaA8az9siFSGxJWo_z')
        # tt3

    def show_seventhtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1zYLLBMAZ0rPa52WH7wza6O5JPwUmubTy')

        # et1

    def show_seventhenglishmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1-lghxs08vJboNAOLssHGOcG9SusRg0Sk')
        # et2

    def show_seventhenglishmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1IlA-Yd1lSXYdy693G2dm8m4vJm_TSjp4')
        # et3

    def show_seventhenglishmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1cfpMFNpkGKuxOC1MtISfx1SqG69Jeml2')
        # mt1

    def show_seventhmathsmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1-XKxJck-uvCHGFLkvMndIqZ7zD2BQeo0')
        # mt2

    def show_seventhmathsmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1kgL3aYJ_yWoatnJ2YOZXpLuD7NoGvved')
        # mt3

    def show_seventhmathsmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1ZMhyYMcoKPWTomS9skYydN2X9DyqXDXq')
        # st1

    def show_seventhsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1-_TOLPPHJVDUKb67V5dqzy8vW422bgGk')
        # st2

    def show_seventhsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1IuWYzA06KVUgOwc-N3j-zzR1AY-Kui_k')
        # st3

    def show_seventhsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1JyfFUEnUfiUgeG4JpzfjtI6DK7XQLxeU')

        # st1

    def show_seventhsocialsciencematerialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1-eLxUwBiZJqMak8b-pBLyEicd1FkF1B9')
        # st2

    def show_seventhsocialsciencematerialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1J0PupWsHj-QqsZa6iki6t8ncscC2ATho')
        # st3

    def show_seventhsocialsciencematerialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1IXuOMCPDBPGNjR9if6CjLJWRtjJvUCSt')

    def show_eightthtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1pyyZJZTxJef5umYtfX5SohNYnZxzBVHY')
        # tt2

    def show_eightthtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1JpFVk5kBQydm1ozcPA5d1qC0xb1fIFaV')
        # tt3

    def show_eightthtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1kyvj10jZu85iF3va2pK50M1BZGqPtn9g')

    def show_eightthtamilmaterialsterm1guide(self):
        wb.open_new(r'https://drive.google.com/file/d/1rafUyLh19LDrpe5_NdIX75bkgP6-5Fwp/view?usp=sharing')
        # tt2

    def show_eightthtamilmaterialsterm2guide(self):
        wb.open_new(r'https://drive.google.com/file/d/1y6v7v7Bn3s6R3MbennnJI1OnceNgx69_/view?usp=sharing')
        # tt3

    def show_eightthtamilmaterialsterm3guide(self):
        wb.open_new(r'https://drive.google.com/file/d/1mq_OGnqAaI8twm2oH-p46n-dtxBJ0f_w/view?usp=sharing')

    def show_eightthtamilmaterialsnewbook(self):
        wb.open_new(r'https://drive.google.com/file/d/10Rk4bD7UxHz3e_HUi3bAet8wxjchhFTI/view?usp=sharing')

        # ***************************************************************************************************************************88

    def show_eightthenglishmaterialsterm1prosec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-prose-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm1prosec2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-prose-chapter-2/')
        # et3

    def show_eightthenglishmaterialsterm1prosec3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-prose-chapter-3/')

    def show_eightthenglishmaterialsterm1poemc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-poem-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm1poemc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-poem-chapter-2/')
        # et3

    def show_eigtthenglishmaterialsterm1poemc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-poem-chapter-3/')

    def show_eightthenglishmaterialsterm1supplementaryc1(self):
        wb.open_new(
            r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-supplementary-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm1supplementaryc2(self):
        wb.open_new(
            r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-supplementary-chapter-2/')
        # et3

    def show_eightthenglishmaterialsterm1supplementaryc3(self):
        wb.open_new(
            r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-1-supplementary-chapter-3/')

    def show_eightthenglishmaterialsterm2prosec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-2-prose-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm2prosec2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-2-prose-chapter-2/')
        # et3

    def show_eightthenglishmaterialsterm2poemc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-3-poem-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm2poemc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-2-poem-chapter-2/')
        # et3

    def show_eightthenglishmaterialsterm2supplementaryc1(self):
        wb.open_new(
            r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-2-supplementary-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm2supplementaryc2(self):
        wb.open_new(
            r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-2-supplementary-chapter-2/')
        # et3

    def show_eightthenglishmaterialsterm3prosec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-3-prose-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm3prosec2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-3-prose-chapter-2/')
        # et3

    def show_eightthenglishmaterialsterm3poemc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-3-poem-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm3poemc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-3-poem-chapter-2/')
        # et3

    def show_eightthenglishmaterialsterm3supplementaryc1(self):
        wb.open_new(
            r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-3-supplementary-chapter-1/')
        # et2

    def show_eightthenglishmaterialsterm3supplementaryc2(self):
        wb.open_new(
            r'https://samacheerkalvi.guru/samacheer-kalvi-8th-english-solutions-term-3-supplementary-chapter-2/')
        # et3

        # **********************************************************************************************************************************

    def show_eightthmathsmaterialsterm1c1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-1-intext-questions/')
        # et2

    def show_eightthmathsmaterialsterm1c1ex1_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-1-ex-1-1/')
        # et3

    def show_eightthmathsmaterialsterm1c1ex1_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-1-ex-1-2/')

    def show_eightthmathsmaterialsterm1c1ex1_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-1-ex-1-3')
        # et2

    def show_eightthmathsmaterialsterm1addc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-1-additional-questions/')
        # et3

    def show_eigtthmathsmaterialsterm1c2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-2-intext-questions/')

    def show_eightthmathsmaterialsterm1c2ex2_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-2-ex-2-1/')
        # et2

    def show_eightthmathsmaterialsterm1c2ex2_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-2-ex-2-2/')
        # et3

    def show_eightthmathsmaterialsterm1c2ex2_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-2-ex-2-3/')

    def show_eightthmathsmaterialsterm1c2ex2_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-2-ex-2-4/')
        # et2

    def show_eightthmathsmaterialsterm1c2add(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-2-additional-questions/')
        # et2

    def show_eightthmathsmaterialsterm1c3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-3-intext-questions/')
        # et2

    def show_eightthmathsmaterialsterm1c3ex3_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-3-ex-3-1/')
        # et3

    def show_eightthmathsmaterialsterm1c3ex3_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-3-ex-3-2/')
        # et2

    def show_eightthmathsmaterialsterm1c3ex3_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-3-ex-3-3/')
        # et3

    def show_eightthmathsmaterialsterm1c3ex3_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-3-ex-3-4/')
        # et2

    def show_eightthmathsmaterialsterm1c3ex3_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-3-ex-3-5/')
        # et3

    def show_eightthmathsmaterialsterm1c3add(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-3-additional-questions/')
        # et2

    def show_eightthmathsmaterialsterm1c4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-4-intext-questions/')
        # et3

    def show_eightthmathsmaterialsterm1c4ex4_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-4-ex-4-1/')
        # et3

    def show_eightthmathsmaterialsterm1c4ex4_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-4-ex-4-2/')
        # et2

    def show_eightthmathsmaterialsterm1c4ex4_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-4-ex-4-3/')
        # et3

    def show_eightthmathsmaterialsterm1c4add(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-4-additional-questions/')

        # et3

    def show_eightthmathsmaterialsterm1c5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-5-intext-questions/')

    def show_eightthmathsmaterialsterm1c5ex5_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-5-ex-5-1/')

    def show_eightthmathsmaterialsterm1c5ex5_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-5-ex-5-2/')

    def show_eightthmathsmaterialsterm1c5ex5_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-5-ex-5-3/')

    def show_eightthmathsmaterialsterm1c5add(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-maths-term-1-chapter-5-additional-questions/')

        # **************************************************************************************

    def show_eightthsciencematerialsterm1c1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-1/')
        # et2

    def show_eightthsciencematerialsterm1c2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-2/')
        # et3

    def show_eightthsciencematerialsterm1c3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-3/')

    def show_eightthsciencematerialsterm1c4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-4/')
        # et2

    def show_eightthsciencematerialsterm1c5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-5/')
        # et3

    def show_eigtthsciencematerialsterm1c6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-6/')

    def show_eightthsciencematerialsterm1c7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-7/')
        # et2

    def show_eightthsciencematerialsterm1c8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-8/')
        # et3

    def show_eightthsciencematerialsterm1c9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-1-chapter-9/')

    def show_eightthsciencematerialsterm2c1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-2-chapter-1/')
        # et2

    def show_eightthsciencematerialsterm2c2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-2-chapter-2/')
        # et2

    def show_eightthsciencematerialsterm2c3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-2-chapter-3/')
        # et2

    def show_eightthsciencematerialsterm2c4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-2-chapter-4/')
        # et3

    def show_eightthsciencematerialsterm2c5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-2-chapter-5/')
        # et2

    def show_eightthsciencematerialsterm2c6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-2-chapter-6/')
        # et3

    def show_eightthsciencematerialsterm2c7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-2-chapter-7/')
        # et2

    def show_eightthsciencematerialsterm3c1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-1/')
        # et3

    def show_eightthsciencematerialsterm3c2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-2/')
        # et2

    def show_eightthsciencematerialsterm3c3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-3/')
        # et3

    def show_eightthsciencematerialsterm3c4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-4/')
        # et3

    def show_eightthsciencematerialsterm3c5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-5/')
        # et2

    def show_eightthsciencematerialsterm3c6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-6/')
        # et3

    def show_eightthsciencematerialsterm3c7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-7/')

        # et3

    def show_eightthsciencematerialsterm3c8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-8/')

    def show_eightthsciencematerialsterm3c9(self):
        wb.open_new(r'//samacheerkalvi.guru/samacheer-kalvi-8th-science-term-3-chapter-9/')

        # ***********************************************************************************************************************************

    def show_eightthsocialsciencematerialsterm1hc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-1-chapter-1/')
        # et2

    def show_eightthsocialsciencematerialsterm1hc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-1-chapter-2/')
        # et3

    def show_eightthsocialsciencematerialsterm1hc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-1-chapter-3/')

    def show_eightthsocialsciencematerialsterm1hc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-1-chapter-4/')
        # et2

    def show_eightthsocialsciencematerialsterm1gc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-1-chapter-1/')
        # et3

    def show_eigtthsocialsciencematerialsterm1gc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-1-chapter-2/')

    def show_eightthsocialsciencematerialsterm1gc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-1-chapter-3/')
        # et2

    def show_eightthsocialsciencematerialsterm1cc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-civics-term-1-chapter-1/')
        # et3

    def show_eightthsocialsciencematerialsterm1cc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-civics-term-1-chapter-2/')

    def show_eightthsocialsciencematerialsterm1ec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-economics-term-1-chapter-1/')
        # et2

    def show_eightthsocialsciencematerialsterm2hc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-2-chapter-1/')
        # et2

    def show_eightthsocialsciencematerialsterm2hc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-2-chapter-2/')
        # et2

    def show_eightthsocialsciencematerialsterm2gc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-2-chapter-1/')
        # et3

    def show_eightthsocialsciencematerialsterm2gc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-2-chapter-2/')
        # et2

    def show_eightthsocialsciencematerialsterm2cc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-civics-term-2-chapter-1/')
        # et3

    def show_eightthsocialsciencematerialsterm2cc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-civics-term-2-chapter-2/')
        # et2

    def show_eightthsocialsciencematerialsterm2cc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-civics-term-2-chapter-3/')
        # et3

    def show_eightthsocialsciencematerialsterm3hc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-3-chapter-1/')
        # et2

    def show_eightthsocialsciencematerialsterm3hc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-history-term-3-chapter-2/')
        # et3

    def show_eightthsocialsciencematerialsterm3gc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-3-chapter-1/')
        # et3

    def show_eightthsocialsciencematerialsterm3gc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-3-chapter-2/')
        # et2

    def show_eightthsocialsciencematerialsterm3gc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-geography-term-3-chapter-3/')
        # et3

    def show_eightthsocialsciencematerialsterm3cc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-civics-term-3-chapter-1/')

        # et3

    def show_eightthsocialsciencematerialsterm3cc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-civics-term-3-chapter-2/')

    def show_eightthsocialsciencematerialsterm3ec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-8th-social-science-economics-term-3-chapter-1/')

        # ****************************************************************************************************************************

    def show_ninethmathsmaterialsterm1c1ex1_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-ex-1-1/')
        # et2

    def show_ninethmathsmaterialsterm1c1ex1_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-ex-1-2/')
        # et3

    def show_ninethmathsmaterialsterm1c1ex1_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-ex-1-3/')

    def show_ninethmathsmaterialsterm1c1ex1_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-ex-1-4/')
        # et2

    def show_ninethmathsmaterialsterm1c1ex1_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-ex-1-5/')
        # et3

    def show_ninethmathsmaterialsterm1c1ex1_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-ex-1-6/')

    def show_ninethmathsmaterialsterm1c1ex1_7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-ex-1-7/')
        # et2

    def show_ninethmathsmaterialsterm1c1add(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-1-additional-questions/')
        # et3

    def show_ninethmathsmaterialsterm1c2ex2_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-1/')

    def show_ninethmathsmaterialsterm1c2ex2_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-2/')
        # et2

    def show_ninethmathsmaterialsterm1c2ex2_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-3/')
        # et2

    def show_ninethmathsmaterialsterm1c2ex2_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-4/')
        # et2

    def show_ninethmathsmaterialsterm1c2ex2_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-5/')
        # et3

    def show_ninethmathsmaterialsterm1c2ex2_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-6/')
        # et2

    def show_ninethmathsmaterialsterm1c2ex2_7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-7/')
        # et3

    def show_ninethmathsmaterialsterm1c2ex2_8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-8/')
        # et2

    def show_ninethmathsmaterialsterm1c2ex2_9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-ex-2-9/')
        # et3

    def show_ninethmathsmaterialsterm1c2add(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-2-additional-questions/')
        # et2

    def show_ninethmathsmaterialsterm1c3ex3_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-1/')
        # et3

    def show_ninethmathsmaterialsterm1c3ex3_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-2/')
        # et3

    def show_ninethmathsmaterialsterm1c3ex3_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-3/')
        # et2

    def show_ninethmathsmaterialsterm1c3ex3_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-4/')
        # et3

    def show_ninethmathsmaterialsterm1c3ex3_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-5/')

        # et3

    def show_ninethmathsmaterialsterm1c3ex3_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-6/')

    def show_ninethmathsmaterialsterm1c3ex3_7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-7/')

    def show_ninethmathsmaterialsterm1c3ex3_8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-8/')

    def show_ninethmathsmaterialsterm1c3ex3_9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-9/')

    def show_ninethmathsmaterialsterm1c3ex3_10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-10/')

    def show_ninethmathsmaterialsterm1c3ex3_11(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-11/')
        # et2

    def show_ninethmathsmaterialsterm1c3ex3_12(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-12/')
        # et3

    def show_ninethmathsmaterialsterm1c3ex3_13(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-13/')

    def show_ninethmathsmaterialsterm1c3ex3_14(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-14/')
        # et2

    def show_ninethmathsmaterialsterm1c3ex3_15(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-3-ex-3-15/')
        # et3

    def show_ninethmathsmaterialsterm1c4ex4_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-4-ex-4-1/')

    def show_ninethmathsmaterialsterm1c4ex4_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-4-ex-4-2/')
        # et2

    def show_ninethmathsmaterialsterm1c4ex4_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-4-ex-4-3/')
        # et3

    def show_ninethmathsmaterialsterm1c4ex4_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-4-ex-4-4/')

    def show_ninethmathsmaterialsterm1c4ex4_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-4-ex-4-5/')
        # et2

    def show_ninethmathsmaterialsterm1c4ex4_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-4-ex-4-6/')
        # et2

    def show_ninethmathsmaterialsterm1c4ex4_7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-4-ex-4-7/')
        # et2

    def show_ninethmathsmaterialsterm1c5ex5_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-5-ex-5-1/')
        # et3

    def show_ninethmathsmaterialsterm1c5ex5_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-5-ex-5-2/')
        # et2

    def show_ninethmathsmaterialsterm1c5ex5_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-5-ex-5-3/')
        # et3

    def show_ninethmathsmaterialsterm1c5ex5_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-5-ex-5-4/')
        # et2

    def show_ninethmathsmaterialsterm1c5ex5_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-5-ex-5-5/')
        # et3

    def show_ninethmathsmaterialsterm1c5ex5_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-5-ex-5-6/')
        # et2

    def show_ninethmathsmaterialsterm1c6ex6_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-6-ex-6-1/')
        # et3

    def show_ninethmathsmaterialsterm1c6ex6_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-6-ex-6-2/')
        # et3

    def show_ninethmathsmaterialsterm1c6ex6_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-6-ex-6-3/')
        # et2

    def show_ninethmathsmaterialsterm1c6ex6_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-6-ex-6-4/')
        # et3

    def show_ninethmathsmaterialsterm1c6ex6_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-6-ex-6-5/')

        # et3

    def show_ninethmathsmaterialsterm1c7ex7_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-7-ex-7-1/')

    def show_ninethmathsmaterialsterm1c7ex7_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-7-ex-7-2/')

    def show_ninethmathsmaterialsterm1c7ex7_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-7-ex-7-3/')

    def show_ninethmathsmaterialsterm1c7ex7_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-7-ex-7-4/')

    def show_ninethmathsmaterialsterm1c8ex8_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-8-ex-8-1/')
        # et2

    def show_ninethmathsmaterialsterm1c8ex8_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-8-ex-8-2/')
        # et3

    def show_ninethmathsmaterialsterm1c8ex8_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-8-ex-8-3/')
        # et2

    def show_ninethmathsmaterialsterm1c8ex8_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-8-ex-8-4/')
        # et3

    def show_ninethmathsmaterialsterm1c9ex9_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-9-ex-9-1/')
        # et2

    def show_ninethmathsmaterialsterm1c9ex9_2(self):
        wb.open_new(r'ttps://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-9-ex-9-2/')
        # et3

    def show_ninethmathsmaterialsterm1c9ex9_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-maths-chapter-9-ex-9-3/')

        # et2
        # ****************************************************************************************************************************

    def show_ninethenglishmaterialsprosec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-prose-chapter-1/')
        # et2

    def show_ninethenglishmaterialsprosec2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-prose-chapter-2/')
        # et3

    def show_ninethenglishmaterialsprosec3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-prose-chapter-3/')

    def show_ninethenglishmaterialsprosec4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-prose-chapter-4/')
        # et2

    def show_ninethenglishmaterialsprosec5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-prose-chapter-5/')
        # et3

    def show_ninethenglishmaterialsprosec6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-prose-chapter-6/')

    def show_ninethenglishmaterialsprosec7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-prose-chapter-7/')
        # et2

    def show_ninethenglishmaterialspoemc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-poem-chapter-1/')
        # et3

    def show_ninethenglishmaterialspoemc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-poem-chapter-2/')

    def show_ninethenglishmaterialspoemc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-poem-chapter-3/')
        # et3

    def show_ninethenglishmaterialspoemc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-poem-chapter-4/')

    def show_ninethenglishmaterialspoemc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-poem-chapter-5/')
        # et3

    def show_ninethenglishmaterialspoemc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-poem-chapter-6/')

    def show_ninethenglishmaterialspoemc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-poem-chapter-7/')
        # et3

    def show_ninethenglishmaterialssupplementaryc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-supplementary-chapter-1/')
        # et2

    def show_ninethenglishmaterialssupplementaryc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-supplementary-chapter-2/')
        # et3

    def show_ninethenglishmaterialssupplementaryc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-supplementary-chapter-3/')

    def show_ninethenglishmaterialssupplementaryc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-supplementary-chapter-4/')
        # et2

    def show_ninethenglishmaterialssupplementaryc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-supplementary-chapter-5/')
        # et3

    def show_ninethenglishmaterialssupplementaryc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-supplementary-chapter-6/')

    def show_ninethenglishmaterialssupplementaryc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-english-solutions-supplementary-chapter-7/')
        # ***********************************************************************************************************************************

    def show_ninethtamilmaterialsterm1(self):
        wb.open_new(r'https://drive.google.com/open?id=1tMBpbDOhjXLa2RyghwyU1A_lVRJUB3ge')
        # tt2

    def show_ninethtamilmaterialsterm2(self):
        wb.open_new(r'https://drive.google.com/open?id=1v9W5_87TIujLr--g_ggPIU8OmVsoGnVJ')
        # tt3

    def show_ninethtamilmaterialsterm3(self):
        wb.open_new(r'https://drive.google.com/open?id=1wU1ztgtp50nsvIoInCmsddHjHFfrY0VT')

    def show_ninethtamilmaterialsguide(self):
        wb.open_new(r'https://www.trbtnpsc.com/2013/09/9th-standard-materials.html')
        # tt2

    def show_ninethtamilmaterialsnewbook(self):
        wb.open_new(r'https://drive.google.com/file/d/1-rN1unqZ7KJUQcwN2M2ocrtGuALz4L6h/view?usp=sharing')
        # ************************************************************************************************************************

    def show_ninethsciencematerialpc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-1/')
        # et2

    def show_ninethsciencematerialspc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-2/')
        # et3

    def show_ninethsciencematerialspc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-3/')

    def show_ninethsciencematerialspc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-4/')
        # et2

    def show_ninethsciencematerialspc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-5/')
        # et3

    def show_ninethsciencematerialspc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-6/')

    def show_ninethsciencematerialspc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-7/')
        # et2

    def show_ninethsciencematerialspc8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-8/')
        # et3

    def show_ninethsciencematerialspc9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-9/')

    def show_ninethsciencematerialschc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-10/')
        # et2

    def show_ninethsciencematerialschc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-11/')
        # et2

    def show_ninethsciencematerialschc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-12/')
        # et2

    def show_ninethsciencematerialschc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-13/')
        # et3

    def show_ninethsciencematerialschc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-14/')

    def show_ninethsciencematerialschc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-15/')
        # et3

    def show_ninethsciencematerialschc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-16/')
        # et2

    def show_ninethsciencematerialschc8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-17/')
        # et3

    def show_ninethsciencematerialschc9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-18/')
        # et2

    def show_ninethsciencematerialschc10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-19/')
        # et3

    def show_ninethsciencematerialschc11(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-20/')
        # et3

    def show_ninethsciencematerialschc12(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-21/')
        # et2

    def show_ninethsciencematerialschc13(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-22/')
        # et3

    def show_ninethsciencematerialschc14(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-23/')

        # et3

    def show_ninethsciencematerialschc15(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-24/')

    def show_ninethsciencematerialschc16(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-25/')

    def show_ninethsciencematerialschc17(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-26/')

    def show_ninethsciencematerialschc18(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-science-solutions-chapter-27/')

        # **************************************************************************88

    def show_ninethsocialsciencematerialshc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-1/')
        # et3

    def show_ninethsocialsciencematerialshc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-2/')

        # et3

    def show_ninethsocialsciencematerialshc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-3/')

    def show_ninethsocialsciencematerialshc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-4/')

    def show_ninethsocialsciencematerialshc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-5/')

    def show_ninethsocialsciencematerialshc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-6/')
        # et3

    def show_ninethsocialsciencematerialshc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-7/')

        # et3

    def show_ninethsocialsciencematerialshc8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-8/')

    def show_ninethsocialsciencematerialshc9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-9/')

    def show_ninethsocialsciencematerialshc10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-10/')

    def show_ninethsocialsciencematerialshc11(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-history-solutions-chapter-11/')

    def show_ninethsocialsciencematerialsgc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-1/')
        # et3

    def show_ninethsocialsciencematerialsgc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-2/ ')

        # et3

    def show_ninethsocialsciencematerialsgc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-3/')

    def show_ninethsocialsciencematerialsgc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-4/')

    def show_ninethsocialsciencematerialsgc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-5/')

    def show_ninethsocialsciencematerialsgc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-6/')
        # et3

    def show_ninethsocialsciencematerialsgc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-7/')

        # et3

    def show_ninethsocialsciencematerialsgc8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-geography-solutions-chapter-8/')

    def show_ninethsocialsciencematerialscc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-civics-solutions-chapter-1/')

    def show_ninethsocialsciencematerialscc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-civics-solutions-chapter-2/')

    def show_ninethsocialsciencematerialscc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-civics-solutions-chapter-3/')

    def show_ninethsocialsciencematerialscc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-civics-solutions-chapter-4/')

    def show_ninethsocialsciencematerialscc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-civics-solutions-chapter-5/')

    def show_ninethsocialsciencematerialscc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-civics-solutions-chapter-6/')

    def show_ninethsocialsciencematerialsec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-economics-solutions-chapter-1/')

    def show_ninethsocialsciencematerialsec2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-economics-solutions-chapter-2/')

    def show_ninethsocialsciencematerialsec3(self):
        wb.open_new(r'//samacheerkalvi.guru/samacheer-kalvi-9th-social-science-economics-solutions-chapter-3/')

    def show_ninethsocialsciencematerialsec4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-economics-solutions-chapter-4/')

    def show_ninethsocialsciencematerialsec5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-9th-social-science-economics-solutions-chapter-5/')

        # *******************************************************************************************************************************88

    def show_tenthmathsmaterialsterm1c1ex1_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-1-ex-1-1/')
        # et2

    def show_tenthmathsmaterialsterm1c1ex1_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-1-ex-1-2/')
        # et3

    def show_tenthmathsmaterialsterm1c1ex1_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-1-ex-1-3/')

    def show_tenthmathsmaterialsterm1c1ex1_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-1-ex-1-4/')
        # et2

    def show_tenthmathsmaterialsterm1c1ex1_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-1-ex-1-5/')
        # et3

    def show_tenthmathsmaterialsterm1c1ex1_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-1-ex-1-6/')

    def show_tenthmathsmaterialsterm1c2ex2_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-1/')

    def show_tenthmathsmaterialsterm1c2ex2_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-2/')
        # et2

    def show_tenthmathsmaterialsterm1c2ex2_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-3/')
        # et2

    def show_tenthmathsmaterialsterm1c2ex2_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-3/')
        # et2

    def show_tenthmathsmaterialsterm1c2ex2_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-5/')
        # et3

    def show_tenthmathsmaterialsterm1c2ex2_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-6/')
        # et2

    def show_tenthmathsmaterialsterm1c2ex2_7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-7/')
        # et3

    def show_tenthmathsmaterialsterm1c2ex2_8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-8/')
        # et2

    def show_tenthmathsmaterialsterm1c2ex2_9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-9/')
        # et3

    def show_tenthmathsmaterialsterm1c2ex2_10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-2-ex-2-10/')
        # et2

    def show_tenthmathsmaterialsterm1c3ex3_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-1/')
        # et3

    def show_tenthmathsmaterialsterm1c3ex3_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-2/')
        # et3

    def show_tenthmathsmaterialsterm1c3ex3_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-3/')
        # et2

    def show_tenthmathsmaterialsterm1c3ex3_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-4/')
        # et3

    def show_tenthmathsmaterialsterm1c3ex3_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-5/')

        # et3

    def show_tenthmathsmaterialsterm1c3ex3_6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-6/')

    def show_tenthmathsmaterialsterm1c3ex3_7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-7/')

    def show_tenthmathsmaterialsterm1c3ex3_8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-8/')

    def show_tenthmathsmaterialsterm1c3ex3_9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-9/')

    def show_tenthmathsmaterialsterm1c3ex3_10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-10/')

    def show_tenthmathsmaterialsterm1c3ex3_11(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-11/')
        # et2

    def show_tenthmathsmaterialsterm1c3ex3_12(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-12/')
        # et3

    def show_tenthmathsmaterialsterm1c3ex3_13(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-13/')

    def show_tenthmathsmaterialsterm1c3ex3_14(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-14/')
        # et2

    def show_tenthmathsmaterialsterm1c3ex3_15(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-15/')
        # et3

    def show_tenthmathsmaterialsterm1c3ex3_16(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-16/')
        # et3

    def show_tenthmathsmaterialsterm1c3ex3_17(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-17/')

    def show_tenthmathsmaterialsterm1c3ex3_18(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-18/')
        # et2

    def show_tenthmathsmaterialsterm1c3ex3_19(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-3-ex-3-19/')

    def show_tenthmathsmaterialsterm1c4ex4_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-4-ex-4-1/')

    def show_tenthmathsmaterialsterm1c4ex4_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-4-ex-4-2/')
        # et2

    def show_tenthmathsmaterialsterm1c4ex4_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-4-ex-4-3/')
        # et3

    def show_tenthmathsmaterialsterm1c4ex4_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-4-ex-4-4/')

    def show_tenthmathsmaterialsterm1c4ex4_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-4-ex-4-5/')
        # et2

    def show_tenthmathsmaterialsterm1c5ex5_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-5-ex-5-1/')
        # et3

    def show_tenthmathsmaterialsterm1c5ex5_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-5-ex-5-2/')
        # et2

    def show_tenthmathsmaterialsterm1c5ex5_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-5-ex-5-3/')
        # et3

    def show_tenthmathsmaterialsterm1c5ex5_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-5-ex-5-4/')
        # et2

    def show_tenthmathsmaterialsterm1c5ex5_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-5-ex-5-5/')
        # et3

    def show_tenthmathsmaterialsterm1c6ex6_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-6-ex-6-1/')
        # et3

    def show_tenthmathsmaterialsterm1c6ex6_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-6-ex-6-2/')
        # et3

    def show_tenthmathsmaterialsterm1c6ex6_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-6-ex-6-3/')
        # et2

    def show_tenthmathsmaterialsterm1c6ex6_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-6-ex-6-4/')
        # et3

    def show_tenthmathsmaterialsterm1c6ex6_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-6-ex-6-5/')

        # et3

    def show_tenthmathsmaterialsterm1c7ex7_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-7-ex-7-1/')

    def show_tenthmathsmaterialsterm1c7ex7_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-7-ex-7-2/')

    def show_tenthmathsmaterialsterm1c7ex7_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-7-ex-7-3/')

    def show_tenthmathsmaterialsterm1c7ex7_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-7-ex-7-4/')

    def show_tenthmathsmaterialsterm1c7ex7_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-7-ex-7-5/')

    def show_tenthmathsmaterialsterm1c8ex8_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-8-ex-8-1/')
        # et2

    def show_tenthmathsmaterialsterm1c8ex8_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-8-ex-8-2/')
        # et3

    def show_tenthmathsmaterialsterm1c8ex8_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-8-ex-8-3/')
        # et2

    def show_tenthmathsmaterialsterm1c8ex8_4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-8-ex-8-4/')
        # et3

    def show_tenthmathsmaterialsterm1c8ex8_5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-maths-chapter-8-ex-8-5/')

        # et2

    def show_tenthsocialsciencematerialshc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-1/')
        # et3

    def show_tenthsocialsciencematerialshc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-2/')

        # et3

    def show_tenthsocialsciencematerialshc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-3/')

    def show_tenthsocialsciencematerialshc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-4/')

    def show_tenthsocialsciencematerialshc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-5/')

    def show_tenthsocialsciencematerialshc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-6/')
        # et3

    def show_tenthsocialsciencematerialshc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-7/')

        # et3

    def show_tenthsocialsciencematerialshc8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-8/')

    def show_tenthsocialsciencematerialshc9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-9/')

    def show_tenthsocialsciencematerialshc10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-history-solutions-chapter-10/')

    def show_tenthsocialsciencematerialsgc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-geography-solutions-chapter-1/')
        # et3

    def show_tenthsocialsciencematerialsgc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-geography-solutions-chapter-2/')

        # et3

    def show_tenthsocialsciencematerialsgc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-geography-solutions-chapter-3/')

    def show_tenthsocialsciencematerialsgc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-geography-solutions-chapter-4/')

    def show_tenthsocialsciencematerialsgc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-geography-solutions-chapter-5/')

    def show_tenthsocialsciencematerialsgc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-geography-solutions-chapter-6/')
        # et3

    def show_tenthsocialsciencematerialsgc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-geography-solutions-chapter-7/')

        # et3

    def show_tenthsocialsciencematerialscc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-civics-solutions-chapter-1/')

    def show_tenthsocialsciencematerialscc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-civics-solutions-chapter-2/')

    def show_tenthsocialsciencematerialscc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-civics-solutions-chapter-3/')

    def show_tenthsocialsciencematerialscc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-civics-solutions-chapter-4/')

    def show_tenthsocialsciencematerialscc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-civics-solutions-chapter-5/')

    def show_tenthsocialsciencematerialsec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-economics-solutions-chapter-1/')

    def show_tenthsocialsciencematerialsec2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-economics-solutions-chapter-2/')

    def show_tenthsocialsciencematerialsec3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-economics-solutions-chapter-3/')

    def show_tenthsocialsciencematerialsec4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-economics-solutions-chapter-4/')

    def show_tenthsocialsciencematerialsec5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-social-science-economics-solutions-chapter-5/')

    def show_tenthenglishmaterialsprosec1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-prose-chapter-1/')
        # et2

    def show_tenthenglishmaterialsprosec2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-prose-chapter-2/')
        # et3

    def show_tenthenglishmaterialsprosec3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-prose-chapter-3/')

    def show_tenthenglishmaterialsprosec4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-prose-chapter-4/')
        # et2

    def show_tenthenglishmaterialsprosec5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-prose-chapter-5/')
        # et3

    def show_tenthenglishmaterialsprosec6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-prose-chapter-6/')

    def show_tenthenglishmaterialsprosec7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-prose-chapter-7/')
        # et2

    def show_tenthenglishmaterialspoemc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-poem-chapter-1/')
        # et3

    def show_tenthenglishmaterialspoemc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-poem-chapter-2/')

    def show_tenthenglishmaterialspoemc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-poem-chapter-3/')
        # et3

    def show_tenthenglishmaterialspoemc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-poem-chapter-4/')

    def show_tenthenglishmaterialspoemc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-poem-chapter-5/')
        # et3

    def show_tenthenglishmaterialspoemc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-poem-chapter-6/')

    def show_tenthenglishmaterialspoemc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-poem-chapter-7/')
        # et3

    def show_tenthenglishmaterialssupplementaryc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-supplementary-chapter-1/')
        # et2

    def show_tenthenglishmaterialssupplementaryc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-supplementary-chapter-2/')
        # et3

    def show_tenthenglishmaterialssupplementaryc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-supplementary-chapter-3/')

    def show_tenthenglishmaterialssupplementaryc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-supplementary-chapter-4/')
        # et2

    def show_tenthenglishmaterialssupplementaryc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-supplementary-chapter-5/')
        # et3

    def show_tenthenglishmaterialssupplementaryc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-supplementary-chapter-6/')

    def show_tenthenglishmaterialssupplementaryc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-english-solutions-supplementary-chapter-7/')

    def show_tenthsciencematerialpc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-1/')
        # et2

    def show_tenthsciencematerialspc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-2/')
        # et3

    def show_tenthsciencematerialspc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-3/')

    def show_tenthsciencematerialspc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-4/')
        # et2

    def show_tenthsciencematerialspc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-5/')
        # et3

    def show_tenthsciencematerialspc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-6/')

    def show_tenthsciencematerialschc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-7/')
        # et2

    def show_tenthsciencematerialschc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-8/')
        # et2

    def show_tenthsciencematerialschc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-9/')
        # et2

    def show_tenthsciencematerialschc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-10/')
        # et3

    def show_tenthsciencematerialschc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-11/')

    def show_tenthsciencematerialsbc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-12/')
        # et3

    def show_tenthsciencematerialsbc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-13/')
        # et2

    def show_tenthsciencematerialsbc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-14/')
        # et3

    def show_tenthsciencematerialsbc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-15/')
        # et2

    def show_tenthsciencematerialsbc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-16/')
        # et3

    def show_tenthsciencematerialsbc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-17/')
        # et3

    def show_tenthsciencematerialsbc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-18/')
        # et2

    def show_tenthsciencematerialsbc8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-19/')
        # et3

    def show_tenthsciencematerialsbc9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-20/')

        # et3

    def show_eleventhenglishmaterialsc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=PgIVrv5JhsE')

    def show_eleventhenglishmaterialsc2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=lYcv31ew-Hg')

    def show_eleventhenglishmaterialsc3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=c6mEAONFlZw')

    def show_eleventhenglishmaterialsc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-english-solutions-prose-chapter-4/')

    def show_eleventhenglishmaterialsc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-english-solutions-prose-chapter-5/')

    def show_eleventhenglishmaterialsc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-english-solutions-prose-chapter-6/')

    def show_tenthsciencematerialsbc10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-21/')

    def show_tenthsciencematerialsbc11(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-22/')

    def show_tenthsciencematerialscsc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-10th-science-solutions-chapter-23/')

    def show_eleventhbiologybotanymaterialschapter1(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-1/')

    def show_eleventhbiologybotanymaterialschapter2(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-2/')

    def show_eleventhbiologybotanymaterialschapter3(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-3/')

    def show_eleventhbiologybotanymaterialschapter4(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-4/')

    def show_eleventhbiologybotanymaterialschapter5(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-5/')

    def show_eleventhbiologybotanymaterialschapter6(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-6/')

    def show_eleventhbiologybotanymaterialschapter7(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-7/')

    def show_eleventhbiologybotanymaterialschapter8(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-8/')

    def show_eleventhbiologybotanymaterialschapter9(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-botany-solutions-chapter-9/')

    def show_eleventhbiologyzoologymaterialschapter1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-1/')

    def show_eleventhbiologyzoologymaterialschapter2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-2/')

    def show_eleventhbiologyzoologymaterialschapter3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-3/')

    def show_eleventhbiologyzoologymaterialschapter4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-4/')

    def show_eleventhbiologyzoologymaterialschapter5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-5/')

    def show_eleventhbiologyzoologymaterialschapter6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-6/')

    def show_eleventhbiologyzoologymaterialschapter7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-7/')

    def show_eleventhbiologyzoologymaterialschapter8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-8/')

    def show_eleventhbiologyzoologymaterialschapter9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-bio-zoology-solutions-chapter-9/')
    def show_eleventhchemistrymaterialschapter1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-1/')

    def show_eleventhchemistrymaterialschapter2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-2/')

    def show_eleventhchemistrymaterialschapter3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-3/')

    def show_eleventhchemistrymaterialschapter4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-4/')

    def show_eleventhchemistrymaterialschapter5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-5/')

    def show_eleventhchemistrymaterialschapter6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-6/')

    def show_eleventhchemistrymaterialschapter7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-7/')

    def show_eleventhchemistrymaterialschapter8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-8/')

    def show_eleventhchemistrymaterialschapter9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-9/')

    def show_eleventhchemistrymaterialschapter10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-10/')

    def show_eleventhchemistrymaterialschapter11(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-11/')

    def show_eleventhchemistrymaterialschapter12(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-12/')

    def show_eleventhchemistrymaterialschapter13(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-13/')

    def show_eleventhchemistrymaterialschapter14(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-14/')

    def show_eleventhchemistrymaterialschapter15(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-chemistry-solutions-chapter-15/')

    def show_eleventhphysicsmaterialschapter1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-1/')

    def show_eleventhphysicsmaterialschapter2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-2/')

    def show_eleventhphysicsmaterialschapter3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-3/')

    def show_eleventhphysicsmaterialschapter4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-4/')

    def show_eleventhphysicsmaterialschapter5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-5/')

    def show_eleventhphysicsmaterialschapter6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-6/')

    def show_eleventhphysicsmaterialschapter7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-7/')

    def show_eleventhphysicsmaterialschapter8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-8/')

    def show_eleventhphysicsmaterialschapter9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-9/')

    def show_eleventhphysicsmaterialschapter10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-physics-solutions-chapter-10/')



    def show_eleventhmathsmaterialsc1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-1-ex-1-1/')

    def show_eleventhmathsmaterialsc2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-1-ex-1-2/')

    def show_eleventhmathsmaterialsc3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-1-ex-1-3/')

    def show_eleventhmathsmaterialsc4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-1-ex-1-4/')

    def show_eleventhmathsmaterialsc5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-1-ex-1-5/')

    def show_eleventhmathsmaterialsc6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-2-ex-2-1/')

    def show_eleventhmathsmaterialsc7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-2-ex-2-2/')

    def show_eleventhmathsmaterialsc8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-11th-maths-solutions-chapter-2-ex-2-4/')

    #teng
    def show_twelthenglishmaterialpoem1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-poem-chapter-1/')

    def show_twelthenglishmaterialprose1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-prose-chapter-1/')

    def show_twelthenglishmaterialsupplymentry1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-supplementary-chapter-1/')

    def show_twelthenglishmaterialpoem2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-poem-chapter-2/')

    def show_twelthenglishmaterialprose2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-prose-chapter-2/')

    def show_twelthenglishmaterialsupplymentry2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-supplementary-chapter-2/')

    def show_twelthenglishmaterialpoem3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-poem-chapter-3/')

    def show_twelthenglishmaterialprose3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-prose-chapter-3/')

    def show_twelthenglishmaterialsupplymentry3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-supplementary-chapter-3/')

    def show_twelthenglishmaterialpoem4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-poem-chapter-4/')

    def show_twelthenglishmaterialprose4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-prose-chapter-4/')

    def show_twelthenglishmaterialsupplymentry4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-supplementary-chapter-4/')

    def show_twelthenglishmaterialpoem5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-poem-chapter-5/')

    def show_twelthenglishmaterialprose5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-prose-chapter-5/')

    def show_twelthenglishmaterialsupplymentry5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-supplementary-chapter-5/')

    def show_twelthenglishmaterialpoem6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-poem-chapter-6/')

    def show_twelthenglishmaterialprose6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-prose-chapter-6/')

    def show_twelthenglishmaterialsupplymentry6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-english-solutions-supplementary-chapter-6/')

    def show_twelthchemistrymaterialschapter1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-1/')

    def show_twelthchemistrymaterialschapter2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-2/')

    def show_twelthchemistrymaterialschapter3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-3/')

    def show_twelthchemistrymaterialschapter4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-4/')

    def show_twelthchemistrymaterialschapter5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-5/')

    def show_twelthchemistrymaterialschapter6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-6/')

    def show_twelthchemistrymaterialschapter7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-7/')

    def show_twelthchemistrymaterialschapter8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-8/')

    def show_twelthchemistrymaterialschapter9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-9/')

    def show_twelthchemistrymaterialschapter10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-10/')

    def show_twelthchemistrymaterialschapter11(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-11/')

    def show_twelthchemistrymaterialschapter12(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-12/')

    def show_twelthchemistrymaterialschapter13(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-13/')

    def show_twelthchemistrymaterialschapter14(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-14/')

    def show_twelthchemistrymaterialschapter15(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-chemistry-solutions-chapter-15/')

    def show_twelthmathsmaterialschapter1ex1_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-1-ex-1-1/')

    def show_twelthmathsmaterialschapter1ex1_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-1-ex-1-2/')

    def show_twelthmathsmaterialschapter1ex1_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-1-ex-1-3/')

    def show_twelthmathsmaterialschapter2ex2_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-2-ex-2-1/')

    def show_twelthmathsmaterialschapter2ex2_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-2-ex-2-2/')

    def show_twelthmathsmaterialschapter2ex2_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-2-ex-2-3/')

    def show_twelthmathsmaterialschapter3ex3_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-3-ex-3-1/')

    def show_twelthmathsmaterialschapter3ex3_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-3-ex-3-2/')

    def show_twelthmathsmaterialschapter3ex3_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-3-ex-3-3/')

    def show_twelthmathsmaterialschapter4ex4_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-4-ex-4-1/')

    def show_twelthmathsmaterialschapter4ex4_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-4-ex-4-2/')

    def show_twelthmathsmaterialschapter4ex4_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-4-ex-4-3/')

    def show_twelthmathsmaterialschapter5ex5_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-5-ex-5-1/')

    def show_twelthmathsmaterialschapter5ex5_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-5-ex-5-2/')

    def show_twelthmathsmaterialschapter5ex5_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-5-ex-5-3/')

    def show_twelthmathsmaterialschapter6ex6_1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-6-ex-6-1/')

    def show_twelthmathsmaterialschapter6ex6_2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-6-ex-6-2/')

    def show_twelthmathsmaterialschapter6ex6_3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-maths-solutions-chapter-6-ex-6-3/')

    def show_twelthphysicsmaterialschapter1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-1/')

    def show_twelthphysicsmaterialschapter2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-2/')

    def show_twelthphysicsmaterialschapter3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-3/')

    def show_twelthphysicsmaterialschapter4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-4/')

    def show_twelthphysicsmaterialschapter5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-5/')

    def show_twelthphysicsmaterialschapter6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-6/')

    def show_twelthphysicsmaterialschapter7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-7/')

    def show_twelthphysicsmaterialschapter8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-8/')

    def show_twelthphysicsmaterialschapter9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-9/')

    def show_twelthphysicsmaterialschapter10(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-physics-solutions-chapter-10/')

    def show_twelthbiologybotanymaterialschapter1(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-1/')

    def show_twelthbiologybotanymaterialschapter2(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-2/')

    def show_twelthbiologybotanymaterialschapter3(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-3/')

    def show_twelthbiologybotanymaterialschapter4(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-4/')

    def show_twelthbiologybotanymaterialschapter5(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-5/')

    def show_twelthbiologybotanymaterialschapter6(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-6/')

    def show_twelthbiologybotanymaterialschapter7(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-7/')

    def show_twelthbiologybotanymaterialschapter8(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-8/')

    def show_twelthbiologybotanymaterialschapter9(self):
        wb.open - new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-botany-solutions-chapter-9/')

    def show_twelthbiologyzoologymaterialschapter1(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-1/')

    def show_twelthbiologyzoologymaterialschapter2(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-2/')

    def show_twelthbiologyzoologymaterialschapter3(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-3/')

    def show_twelthbiologyzoologymaterialschapter4(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-4/')

    def show_twelthbiologyzoologymaterialschapter5(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-5/')

    def show_twelthbiologyzoologymaterialschapter6(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-6/')

    def show_twelthbiologyzoologymaterialschapter7(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-7/')

    def show_twelthbiologyzoologymaterialschapter8(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-8/')

    def show_twelthbiologyzoologymaterialschapter9(self):
        wb.open_new(r'https://samacheerkalvi.guru/samacheer-kalvi-12th-bio-zoology-solutions-chapter-9/')

    def show_prekgtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/V0CF6VatZwE')

    def show_prekgtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/M7Ip6wb7VqM')

    def show_prekgtamilvideosc3(self):
        wb.open_new(r'https://youtu.be/tHRy1RqbGRE')

    def show_prekgenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/-ZNMP1GINzs')

    def show_prekgenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/23_mESawEEc')

    def show_prekgenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/0oKreL1jvkg')

    def show_prekgmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/voCrQ1ebEdU')

    def show_prekgmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/fHqjNHxmB7c')

    def show_prekgsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/2Si7YRqi2v4')

    def show_prekgsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/nZIIfNX_mb0')

    def show_lkgenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/aUCIF8rU0UM')

    def show_lkgenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/1dttq5p0xUM')

    def show_lkgtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/eSMHcI9g41k')

    def show_lkgtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/cjSgSXHX0Dg')

    def show_lkgtamilvideosc3(self):
        wb.open_new(r'https://youtu.be/xCu3t4OPlOk')

    def show_lkgmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/YRl4VyAIJhM')

    def show_lkgmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/WC_SBmoXrUw')

    def show_lkgsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/-y52HTyc3iM')

    def show_lkgsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/xw-S3Gj2J1o')

    def show_ukgenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/RUSCz41aDug')

    def show_ukgenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/rwxWKP4Ld8s')

    def show_ukgtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/pKcsBSaykEc')

    def show_ukgtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/Us6NO6aJiWY')

    def show_ukgmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/Ji8vsdXHYR4')

    def show_ukgmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/ubAMhqUHE7Y')

    def show_ukgsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/_6cG913j6kc')

    def show_ukgsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/McVQ-ssbib8')

    def show_firstenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/cSDm264JLLQ')

    def show_firstenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/Q1Tnni_QHN0')

    def show_firstenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/kfD5hHkzcjM')

    def show_firstenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/sAc2Yu4ne1Y')

    def show_firstenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/MvHlxPNimgc')

    def show_firstenglishvideosc6(self):
        wb.open_new(r'https://youtu.be/TIi2e6ZGpNs')

    def show_firsttamilvideosc1(self):
        wb.open_new(r'https://youtu.be/BA0tsnhtlIg')

    def show_firsttamilvideosc2(self):
        wb.open_new(r'https://youtu.be/CSgfngzHSb0')

    def show_firsttamilvideosc3(self):
        wb.open_new(r'https://youtu.be/DSAmXhD0ASI')

    def show_firsttamilvideosc4(self):
        wb.open_new(r'https://youtu.be/nOI0DoKN3Us')

    def show_firsttamilvideosc5(self):
        wb.open_new(r'https://youtu.be/X3eJnOouglQ')

    def show_firsttamilvideosc6(self):
        wb.open_new(r'https://youtu.be/k4g1unSRseQ')

    def show_firstmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/lGfWirQASMA')

    def show_firstmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/iF91axh0LeY')

    def show_firstmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/AvwX6D5Mc-M')

    def show_firstmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/f76t_nSuE-8')

    def show_firstmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/0nZVjoYqT0k')

    def show_firstmathsvideosc6(self):
        wb.open_new(r'https://youtu.be/PTpUPJP8pMw')

    def show_firstmathsvideosc7(self):
        wb.open_new(r'https://youtu.be/PTpUPJP8pMw')

    def show_firstsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/ZuT-Sh_f6go')

    def show_firstsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/NYjDpw8vL-s')

    def show_firstsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/RxZQWBZ4hic')

    def show_firstsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/mXMofxtDPUQ')

    def show_firstsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/M-ZdqFwayrU')

    def show_firstsciencevideosc6(self):
        wb.open_new(r'https://youtu.be/J7xKgVSCYJA')

    def show_secondenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/Svk3PueMcVU')

    def show_secondenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/9AnXUVidO6w')

    def show_secondenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/QD8WgUz3uUU')

    def show_secondenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/cp-shzfn1s0')

    def show_secondenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/EH-VBvnGFpE')

    def show_secondtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/1-fTw7p_BgU')

    def show_secondtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/cgoKVWwME1Q')

    def show_secondtamilvideosc3(self):
        wb.open_new(r'https://youtu.be/TfjQ-xXRI9o')

    def show_secondtamilvideosc4(self):
        wb.open_new(r'https://youtu.be/3eoL6wTWJcY')

    def show_secondtamilvideosc5(self):
        wb.open_new(r'https://youtu.be/h_36NFXTby0')

    def show_secondtamilvideosc6(self):
        wb.open_new(r'https://youtu.be/awtDcPhx0VU')

    def show_secondmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/1ZB5g9FMMdk')

    def show_secondmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/AmSnmp09nkE')

    def show_secondmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/LgE3WPLKmBo')

    def show_secondmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/TYagY8bs3mg')

    def show_secondmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/ajckymXxt1E')

    def show_secondsciencevideosc1(self):
        wb.open_new('https://youtu.be/hWkKSkI3gkU')

    def show_secondsciencevideosc2(self):
        wb.open_new('https://youtu.be/2VjMYI_sokE')

    def show_secondsciencevideosc3(self):
        wb.open_new('https://youtu.be/18amLZ9vfG8')

    def show_secondsciencevideosc4(self):
        wb.open_new('https://youtu.be/PQwuog7_wmg')

    def show_thirdenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/T6-tJlDTigI')

    def show_thirdenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/bJjPaNdwZ_A')

    def show_thirdenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/3KIUVWelZmo')

    def show_thirdenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/l2_CzEISiR0')

    def show_thirdenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/Yq2ipM6vVD0')

    def show_thirdenglishvideosc6(self):
        wb.open_new(r'https://youtu.be/or4P6Pl-vig')

    def show_thirdtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/qleCPpTfx9w')

    def show_thirdtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/Uj6dmVWO1Gc')

    def show_thirdtamilvideosc3(self):
        wb.open_new(r'https://youtu.be/PmRQzIDLYwE')

    def show_thirdtamilvideosc4(self):
        wb.open_new(r'https://youtu.be/VHYyuYk6k5Q')

    def show_thirdtamilvideosc5(self):
        wb.open_new(r'https://youtu.be/95kHMvD5tfQ')

    def show_thirdtamilvideosc6(self):
        wb.open_new(r'https://youtu.be/UeOr8IAF8PM')

    def show_thirdtamilvideosc7(self):
        wb.open_new(r'https://youtu.be/Tt5stKxkxEU')

    def show_thirdmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/QvrhSXLlKgA')

    def show_thirdmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/_H0VjhTLxqA')

    def show_thirdmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/DS7lRoD2qsE')

    def show_thirdmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/evMt1gFrzrM')

    def show_thirdmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/LD4zp8ruvaI')

    def show_thirdsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/p3Jyo8NGyuw')

    def show_thirdsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/ARR2-2NkKXw')

    def show_thirdsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/s9J0htDif6U')

    def show_thirdsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/cXjCjKuVM5U')

    def show_thirdsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/Lw_DLrxc8AE')

    def show_thirdsocialsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/TLoI8S_hDYU')

    def show_thirdsocialsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/JnVsoZA4x_I')

    def show_thirdsocialsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/dL5qGWaDkC0')

    def show_thirdsocialsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/30Yur2OJZDM')

    def show_fourthenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/bqNjlEsTJt4')

    def show_fourthenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/Jn0M8w0rip4')

    def show_fourthenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/mUjB2TLXsls')

    def show_fourthenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/0U7QS0_W5-c')

    def show_fourthenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/G33lr5SRXoM')

    def show_fourthenglishvideosc6(self):
        wb.open_new(r'https://youtu.be/G3Fm1OhMs8k')

    def show_fourthtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/WOY2PmH85Lw')

    def show_fourthtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/lRVOmYRoxxw')

    def show_fourthtamilvideosc3(self):
        wb.open_new(r'https://youtu.be/bLU09eR7q5A')

    def show_fourthtamilvideosc4(self):
        wb.open_new(r'https://youtu.be/4KivuuhTaHE')

    def show_fourthtamilvideosc5(self):
        wb.open_new(r'https://youtu.be/WPl2DCp-e_s')

    def show_fourthtamilvideosc6(self):
        wb.open_new(r'https://youtu.be/JOQ05m8LzYE')

    def show_fourthmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/4ojLMsTPwJM')

    def show_fourthmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/T8Kgiikuiws')

    def show_fourthmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/KhT4GqhxEf4')

    def show_fourthmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/wHD2T0qnb7o')

    def show_fourthmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/C-vnEJkvUh8')

    def show_fourthmathsvideosc6(self):
        wb.open_new(r'https://youtu.be/KFzcwWTEDDI')

    def show_fourthsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/SYQHGlbEICo')

    def show_fourthsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/Ya17gVIxql0')

    def show_fourthsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/E0rPupQb8DY')

    def show_fourthsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/OYIJQSoMTtA')

    def show_fourthsocialsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/9ZSfQ-gJPzo')

    def show_fourthsocialsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/h-7b3JlKAt4')

    def show_fourthsocialsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/6PVNdIj6KbI')

    def show_fourthsocialsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/VbvSvsTm8f4')

    def show_fourthsocialsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/hsJDy0lcxi8')

    def show_fifthenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/-mZE-wHqLTo')

    def show_fifthenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/egk4iSsInBg')

    def show_fifthenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/OpmIXlRDA9U')

    def show_fifthenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/C6_cgb3yuPc')

    def show_fifthenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/hrj60RFuugA')

    def show_fifthetamilvideosc1(self):
        wb.open_new(r'https://youtu.be/v5y__sgw-q8')

    def show_fifthetamilvideosc2(self):
        wb.open_new(r'https://youtu.be/rxsFoleNruw')

    def show_fifthetamilvideosc3(self):
        wb.open_new(r'https://youtu.be/k2m91LpoiaA')

    def show_fifthetamilvideosc4(self):
        wb.open_new(r'https://youtu.be/9TWw-KfG_qw')

    def show_fifthetamilvideosc5(self):
        wb.open_new(r'https://youtu.be/YewAbTToNOI')

    def show_fifthetamilvideosc6(self):
        wb.open_new(r'https://youtu.be/JK8PKz-42fU')

    def show_fifthemathsvideosc1(self):
        wb.open_new(r'https://youtu.be/W7QLWgBO7S8')

    def show_fifthemathsvideosc2(self):
        wb.open_new(r'https://youtu.be/9c1ga094KIQ')

    def show_fifthemathsvideosc3(self):
        wb.open_new(r'https://youtu.be/4F-XF-1a82I')

    def show_fifthemathsvideosc4(self):
        wb.open_new(r'https://youtu.be/4xnEe8zO1ac')

    def show_fifthemathsvideosc5(self):
        wb.open_new(r'https://youtu.be/odGI-zzLz_I')

    def show_fifthsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/FeiBY9Xs2q4')

    def show_fifthsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/qNTOq1uEObc')

    def show_fifthsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/WHxJJ2jduHU')

    def show_fifthsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/R5s-zxzOMXE')

    def show_fifthsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/rdjwsyBYWQ8')

    def show_fifthsocialsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/MzdrRyLMQ2w')

    def show_fifthsocialsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/aloTF_xN0fQ')

    def show_fifthsocialsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/6R9QmZ8AhK0')

    def show_fifthsocialsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/gZGjSpBehpM')

    def show_fifthsocialsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/q4vsvvF1oXs')

    def show_fifthsocialsciencevideosc6(self):
        wb.open_new(r'https://youtu.be/lwsOWOLgoJ8')

    def show_sixthenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/GhkU7_9TIU0')

    def show_sixthenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/_Szz9v28360')

    def show_sixthenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/1j10fPe4rhg')

    def show_sixthenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/LwuJeLVW3b8')

    def show_sixthenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/6GV4pWdWvDY')

    def show_sixthenglishvideosc6(self):
        wb.open_new(r'https://youtu.be/2vci78GncQI')

    def show_sixthetamilvideosc1(self):
        wb.open_new(r'https://youtu.be/9zuBQF9hM0A')

    def show_sixthetamilvideosc2(self):
        wb.open_new(r'https://youtu.be/5I8i8zHRY4o')

    def show_sixthetamilvideosc3(self):
        wb.open_new(r'https://youtu.be/hEdq-aKGNaU')

    def show_sixthetamilvideosc4(self):
        wb.open_new(r'https://youtu.be/qPaPhGQhzno')

    def show_sixthetamilvideosc5(self):
        wb.open_new(r'https://youtu.be/pKJNQnA8yTI')

    def show_sixthemathsvideosc1(self):
        wb.open_new(r'https://youtu.be/v1wyD95AEmA')

    def show_sixthemathsvideosc2(self):
        wb.open_new(r'https://youtu.be/N3HDPykunrg')

    def show_sixthemathsvideosc3(self):
        wb.open_new(r'https://youtu.be/ZorAMH4rfPY')

    def show_sixthemathsvideosc4(self):
        wb.open_new(r'https://youtu.be/akvRHcXZKV8')

    def show_sixthemathsvideosc5(self):
        wb.open_new(r'https://youtu.be/PNyF-CRr5_4')

    def show_sixthemathsvideosc6(self):
        wb.open_new(r'https://youtu.be/3_SV3_z3LdE')

    def show_sixthemathsvideosc7(self):
        wb.open_new(r'https://youtu.be/e7-JgxIpagY')

    def show_sixthsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/AYGszDkLTdo')

    def show_sixthsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/YGZ8EDwb28U')

    def show_sixthsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/pAZUrlKk6CE')

    def show_sixthsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/wQFhjqKMBAI')

    def show_sixthsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/zyQRZ_xgs6Q')

    def sixthsocialsciencevideosc1(self):
        wb.open_new('https://youtu.be/NAvOg8Dzw_8')

    def sixthsocialsciencevideosc2(self):
        wb.open_new('https://youtu.be/BRUOAEJjp6k')

    def sixthsocialsciencevideosc3(self):
        wb.open_new('https://youtu.be/dh6AejuaXk8')

    def sixthsocialsciencevideosc4(self):
        wb.open_new('https://youtu.be/ArBYU1SPZ48')

    def sixthsocialsciencevideosc5(self):
        wb.open_new('https://youtu.be/jFjI6y46QRk')

    def show_seventhtamilvideosterm1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=ljxwK9N1ais')
        # tt2

    def show_seventhtamilvideosterm2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=yCgg210ycdY')
        # tt3

    def show_seventhtamilvideosterm3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=mFFdjk0Ea5U')

    def show_seventhenglishvideosterm1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=fecYF9bZqJs&list=PL_W4gCqGWB2qsm2HBd9kwE_UoqLqPvQVQ&index=3')
        # tt2

    def show_seventhenglishvideosterm2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=4AnJlprUP4s&list=PL_W4gCqGWB2qsm2HBd9kwE_UoqLqPvQVQ&index=2')
        # tt3

    def show_seventhenglishvideosterm3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=v3sfed_v4pU&list=PL_W4gCqGWB2qsm2HBd9kwE_UoqLqPvQVQ&index=1')

    def show_seventhmathsvideosterm1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=0_kKjFLwCuk')
        # tt2

    def show_seventhmathsvideosterm2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=9qgZdhAYV7w')
        # tt3

    def show_seventhmathsvideosterm3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=rP8YcyPgdRA')

    def show_seventhsciencevideosterm1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=weYbsHEa1RY')
        # tt2

    def show_seventhsciencevideosterm2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=us-CMJS_Zpc')
        # tt3

    def show_seventhsciencevideosterm3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=cAPOXnOhGH8')

    def show_seventhsocialsciencevideosterm1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=rHmRZgdh5iE')
        # tt2

    def show_seventhsocialsciencevideosterm2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=UAHy7g60Y24')
        # tt3

    def show_seventhsocialsciencevideosterm3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=5higZIrcrKM')

    def show_eightthtamilvideosterm1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=OsxZQrSzRQk')
        # tt2

    def show_eightthtamilvideosterm2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=zxHGxiXFqRI')
        # tt3

    def show_eightthtamilvideosterm3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=s3zGK_w7vGc')

    def show_eightthenglishvideosterm1prosec1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=nrVbQ2e8_c8')
        # et2

    def show_eightthenglishvideosterm1prosec2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=JD50zJUXuc8')
        # et3

    def show_eightthenglishvideosterm1prosec3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=qEuI2eP6J_M')

    def show_eightthenglishvideosterm1poemc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=LGz4XXXdUxs')
        # et2

    def show_eightthenglishvideosterm1poemc2(self):
        wb.open_new(r'https://www.youtube.com/results?search_query=eightth+standard+english+term1+unit+2poem')
        # et3

    def show_eigtthenglishvideosterm1poemc3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=NjoN_JR2BYg')

    def show_eightthenglishvideosterm1supplementaryc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=TJTzauARBlU')
        # et2

    def show_eightthenglishvideosterm1supplementaryc2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=TFFH45bZe1I')
        # et3

    def show_eightthenglishvideosterm1supplementaryc3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=1aYY8t6nRrE')

    def show_eightthenglishvideosterm2prosec1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=EeF5c7uN9jA')
        # et2

    def show_eightthenglishvideosterm2prosec2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=vqFXYLzIXJ0')
        # et3

    def show_eightthenglishvideosterm2poemc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=LGz4XXXdUxs')
        # et2

    def show_eightthenglishvideosterm2poemc2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=XI7BC9lM-iA')
        # et3

    def show_eightthenglishvideosterm2supplementaryc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=a3unQnpiizk')
        # et2

    def show_eightthenglishvideosterm2supplementaryc2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=fGh9dtq_u4U')
        # et3

    def show_eightthenglishvideosterm3prosec1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=OCi7h9IdH0Y')
        # et2

    def show_eightthenglishvideosterm3poemc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=TXtC8RMMh1g')
        # et2

    def show_eightthenglishvideosterm3supplementaryc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=nqIRiO8Mih4')
        # et2

    def show_eightthmathsvideosc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=dJi95fukxVc&list=PLZTYHUY2zirGMmya5XWlgeBMLtxLqyFiW')

    # et2

    def show_eightthmathsvideosc2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=OCShHKujciE&list=PLZTYHUY2zirGMmya5XWlgeBMLtxLqyFiW&index=2')

    # et3

    def show_eightthmathsvideosc3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=N-_4eaDHqyo&list=PLZTYHUY2zirGMmya5XWlgeBMLtxLqyFiW&index=3')

    # et2

    def show_eightthmathsvideosc4(self):
        wb.open_new(r'https://www.youtube.com/watch?v=M2-26qmzHBE&list=PLZTYHUY2zirGMmya5XWlgeBMLtxLqyFiW&index=4')

    # et3

    def show_eightthmathsvideosc5(self):
        wb.open_new(r'https://www.youtube.com/watch?v=tXmX0ES4y4w&list=PLZTYHUY2zirGMmya5XWlgeBMLtxLqyFiW&index=5')

    # et2

    def show_eightthmathsvideosc6(self):
        wb.open_new(r'https://www.youtube.com/watch?v=hSaTuHoea_w&list=PLZTYHUY2zirGMmya5XWlgeBMLtxLqyFiW&index=6')

    def show_eightthmathsvideosc7(self):
        wb.open_new(r'https://www.youtube.com/watch?v=Ygs1Llu75W4&list=PLZTYHUY2zirGMmya5XWlgeBMLtxLqyFiW&index=7')

    def show_eightthsciencevideosc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=XyOy4ZVdbmQ')

    # et2

    def show_eightthsciencevideosc2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=WwW-xzOL1A4')

    # et3

    def show_eightthsciencevideosc3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=K5kJZ-SfGBg')

    # et2

    def show_eightthsciencevideosterm1c4(self):
        wb.open_new(r'https://www.youtube.com/watch?v=oqGVi4nzRsg')

    # et3

    def show_eightthsciencevideosc5(self):
        wb.open_new(r'https://www.youtube.com/watch?v=AMklgpJT3hU')

    # et2

    def show_eightthsciencevideosc6(self):
        wb.open_new(r'https://www.youtube.com/watch?v=yf1J0PFTtCA')

    def show_eightthsciencevideosc7(self):
        wb.open_new(r'https://www.youtube.com/watch?v=zoHrCz8aC4M')

    def show_eightthsocialsciencevideosc1(self):
        wb.open_new(r'https://www.youtube.com/watch?v=FHCz2WdfWKY')

    # et2

    def show_eightthsocialsciencevideosc2(self):
        wb.open_new(r'https://www.youtube.com/watch?v=Y7IXBEUo8oM')

    # et3

    def show_eightthsocialsciencevideosc3(self):
        wb.open_new(r'https://www.youtube.com/watch?v=C0UHCZsGrNo')

    # et2

    def show_eightthsocialsciencevideosc4(self):
        wb.open_new(r'https://www.youtube.com/watch?v=OjUJVAoCznM')

    def show_eightthsocialsciencevideosc5(self):
        wb.open_new(r'https://www.youtube.com/watch?v=MHDoJZM4NRY')

    # et2

    def show_eightthsocialsciencevideosc6(self):
        wb.open_new(r'https://www.youtube.com/watch?v=DlorSQz4ido')

    def show_eightthsocialsciencevideosc7(self):
        wb.open_new(r'https://www.youtube.com/watch?v=btIkf1nSDJ0')

    def show_eightthsocialsciencevideosc8(self):
        wb.open_new(r'https://www.youtube.com/watch?v=n05br00PXZo')

    # et2

    def show_eightthsocialsciencevideosc9(self):
        wb.open_new(r'https://www.youtube.com/watch?v=OGV2pE8iEpY')

    def show_ninethenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/ttto-cEqILY')

    def show_ninethenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/iyg_D5s4rss')

    def show_ninethenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/3CFORHIbMGk')

    def show_ninethenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/84EICYDpZwk')

    def show_ninethenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/d5wzCDPpdRg')

    def show_ninethtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/gVkUi66xxmk')

    def show_ninethtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/1mV-75ATUvM')

    def show_ninethtamilvideosc3(self):
        wb.open_new(r'https://youtu.be/p5CV2UcfJcI')

    def show_ninethtamilvideosc4(self):
        wb.open_new(r'https://youtu.be/_dai_43hHck')

    def show_ninethtamilvideosc5(self):
        wb.open_new(r'https://youtu.be/WX52ts_91JQ')

    def show_ninethtamilvideosc6(self):
        wb.open_new(r'https://youtu.be/-tckUPcy4A4')

    def show_ninethmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/06ou1bXXyy4')

    def show_ninethmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/vuAtBiCyd2U')

    def show_ninethmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/4Vbq0eN-QU8')

    def show_ninethmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/OsrwwEOYl6c')

    def show_ninethmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/iJ-5PpA19us')

    def show_ninethmathsvideosc6(self):
        wb.open_new(r'https://youtu.be/BPeKAlbUkEs')

    def show_ninethmathsvideosc7(self):
        wb.open_new(r'https://youtu.be/-iOeSrqi3gU')

    def show_ninethmathsvideosc8(self):
        wb.open_new(r'https://youtu.be/gvHL2O8w2WM')

    def show_ninethmathsvideosc9(self):
        wb.open_new(r'https://youtu.be/72KUW37Kodc')

    def show_ninethsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/5XycC4Mlsvk')

    def show_ninethsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/zdzSnYyTHjY')

    def show_ninethsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/X6KMq2kZmFo')

    def show_ninethsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/hNcFZ8SCJlQ')

    def show_ninethsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/QO5UsqcOTgY')

    def show_ninethsciencevideosc6(self):
        wb.open_new(r'https://youtu.be/qJELpnMKXDk')

    def show_ninethsciencevideosc7(self):
        wb.open_new(r'https://youtu.be/UFg5P5SuAm8')

    def show_ninethsciencevideosc8(self):
        wb.open_new(r'https://youtu.be/azaPWifb_-E')

    def show_ninethsocialsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/gY-7kUlOmns')

    def show_ninethsocialsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/132rQEcxHv0')

    def show_ninethsocialsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/8UVB0AD016I')

    def show_ninethsocialsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/kO7KpL5lFoQ')

    def show_ninethsocialsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/b4nhO0X5nT0')

    def show_ninethsocialsciencevideosc6(self):
        wb.open_new(r'https://youtu.be/qJmg7qzUVGM')

    def show_ninethsocialsciencevideosc7(self):
        wb.open_new(r'https://youtu.be/_rcEI6bc38I')

    def show_ninethsocialsciencevideosc8(self):
        wb.open_new(r'https://youtu.be/kgQ5aRQq_M0')

    def show_tenthenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/aTY9t_iQ73o')

    def show_tenthenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/Sz5p4cdZ750')

    def show_tenthenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/MaJ6KNxmAnU')

    def show_tenthenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/1i2ppWu3MpA')

    def show_tenthenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/tyX9oeTcSjI')

    def show_tenthenglishvideosc6(self):
        wb.open_new(r'https://youtu.be/CU9sPQYBNMA')

    def show_tenthenglishvideosc7(self):
        wb.open_new(r'https://youtu.be/_VUhVoZ806c')

    def show_tenthtamilvideosc1(self):
        wb.open_new(r'https://youtu.be/QZQZq9K7qFI')

    def show_tenthtamilvideosc2(self):
        wb.open_new(r'https://youtu.be/DTodUpoKyPc')

    def show_tenthtamilvideosc3(self):
        wb.open_new(r'https://youtu.be/N8T6MGPXU6s')

    def show_tenthtamilvideosc4(self):
        wb.open_new(r'https://youtu.be/iVZ13Pw8Qm8')

    def show_tenthtamilvideosc5(self):
        wb.open_new(r'https://youtu.be/BjSDXQ28GM0')

    def show_tenthtamilvideosc6(self):
        wb.open_new(r'https://youtu.be/nuiFLKEMZR0')

    def show_tenthtamilvideosc7(self):
        wb.open_new(r'https://youtu.be/VQkb243Ev1Q')

    def show_tenthtamilvideosc8(self):
        wb.open_new(r'https://youtu.be/DpB2Q5XXbY8')

    def show_tenthmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/hWe-X9gfwQg')

    def show_tenthmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/IuRBWkc0gfk')

    def show_tenthmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/JYwYnSETYrQ')

    def show_tenthmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/GB4DcKcxySA')

    def show_tenthmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/HmgDtrGHU_Y')

    def show_tenthmathsvideosc6(self):
        wb.open_new(r'https://youtu.be/APi0M0K3Fyg')

    def show_tenthmathsvideosc7(self):
        wb.open_new(r'https://youtu.be/PXpzOoklwTc')

    def show_tenthmathsvideosc8(self):
        wb.open_new(r'https://youtu.be/UP7f_5AJWDk')

    def show_tenthmathsvideosc9(self):
        wb.open_new(r'https://youtu.be/L7Tn0cveJyw')

    def show_tenthsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/uaViGD6cPJ4')

    def show_tenthsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/7bUa3eMIyRk')

    def show_tenthsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/HyFuW9jVo9w')

    def show_tenthsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/5Q9LgvQs5Nw')

    def show_tenthsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/Saqbd4RTpKM')

    def show_tenthsciencevideosc6(self):
        wb.open_new(r'https://youtu.be/OAvapO36RIw')

    def show_tenthsciencevideosc7(self):
        wb.open_new(r'https://youtu.be/xLEPGJ4bjEs')

    def show_tenthsciencevideosc8(self):
        wb.open_new(r'https://youtu.be/g550H4e5FCY')

    def show_tenthsocialsciencevideosc1(self):
        wb.open_new(r'https://youtu.be/D19ngSEisDc')

    def show_tenthsocialsciencevideosc2(self):
        wb.open_new(r'https://youtu.be/6MzS5G4_rKs')

    def show_tenthsocialsciencevideosc3(self):
        wb.open_new(r'https://youtu.be/DSo771Sn5Ik')

    def show_tenthsocialsciencevideosc4(self):
        wb.open_new(r'https://youtu.be/zo-VF8zH9eM')

    def show_tenthsocialsciencevideosc5(self):
        wb.open_new(r'https://youtu.be/eYnhFY0bLLU')

    def show_tenthsocialsciencevideosc6(self):
        wb.open_new(r'https://youtu.be/iO4eT4wa3zI')

    def show_tenthsocialsciencevideosc7(self):
        wb.open_new(r'https://youtu.be/MZtfrAp-t4w')

    def show_tenthsocialsciencevideosc8(self):
        wb.open_new(r'https://youtu.be/I154YKY8WO4')

    def show_eleventhenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/Ty8kgJnX7FY')

    def show_eleventhenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/IlqcxuiUBvI')

    def show_eleventhenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/kK7_XBgKQ04')

    def show_eleventhenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/eXlAsp7Zqzw')

    def show_eleventhenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/_Ns0t7wKk48')

    def show_eleventhenglishvideosc6(self):
        wb.open_new(r'https://youtu.be/H7EsCO0u9jo')

    def show_eleventhenglishvideosc7(self):
        wb.open_new(r'https://youtu.be/XBBmazLHePg')

    def show_eleventhenglishvideosc8(self):
        wb.open_new(r'https://youtu.be/NE8IVEpNhwA')

    def show_eleventhenglishvideosc9(self):
        wb.open_new(r'https://youtu.be/cxIlVTf5Iz0')

    def show_eleventhmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/tyDKR4FG3Yw')

    def show_eleventhmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/itrXYg41-V0')

    def show_eleventhmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/4TlCToZZ5gA')

    def show_eleventhmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/sRDwsfNDXak')

    def show_eleventhmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/CSALbevEMfs')

    def show_eleventhmathsvideosc6(self):
        wb.open_new(r'https://youtu.be/BxQPdvNRqrc')

    def show_eleventhmathsvideosc7(self):
        wb.open_new(r'https://youtu.be/5u6HUlPzEjU')

    def show_eleventhmathsvideosc8(self):
        wb.open_new(r'https://youtu.be/TA189Lct1Tw')

    def show_eleventhchemistryvideosc1(self):
        wb.open_new(r'https://youtu.be/KjUe6XxIi4M')

    def show_eleventhchemistryvideosc2(self):
        wb.open_new(r'https://youtu.be/GKhhbhTjStY')

    def show_eleventhchemistryvideosc3(self):
        wb.open_new(r'https://youtu.be/Zg6KeXsDVwY')

    def show_eleventhchemistryvideosc4(self):
        wb.open_new(r'https://youtu.be/H03cj53KMx0')

    def show_eleventhchemistryvideosc5(self):
        wb.open_new(r'https://youtu.be/lz7irIuBbR0')

    def show_eleventhchemistryvideosc6(self):
        wb.open_new(r'https://youtu.be/jKafO6OGJGY')

    def show_eleventhchemistryvideosc7(self):
        wb.open_new(r'https://youtu.be/NQKOmk08cUQ')

    def show_eleventhchemistryvideosc8(self):
        wb.open_new(r'https://youtu.be/wlD_ImYQAgQ')

    def show_eleventhphysicsvideosc1(self):
        wb.open_new(r'https://youtu.be/oOCcpGA0ba0')

    def show_eleventhphysicsvideosc2(self):
        wb.open_new(r'https://youtu.be/z220t0L17EA')

    def show_eleventhphysicsvideosc3(self):
        wb.open_new(r'https://youtu.be/sgCtgo4L0vM')

    def show_eleventhphysicsvideosc4(self):
        wb.open_new(r'https://youtu.be/lD8xWNv1_4o')

    def show_eleventhphysicsvideosc5(self):
        wb.open_new(r'https://youtu.be/erghLWXDScI')

    def show_eleventhphysicsvideosc6(self):
        wb.open_new(r'https://youtu.be/c9shwPMpSq8')

    def show_eleventhphysicsvideosc7(self):
        wb.open_new(r'https://vimeo.com/435465360')

    def show_eleventhphysicsvideosc8(self):
        wb.open_new(r'https://youtu.be/RA7gU-P03XU')

    def show_eleventhbiologyvideosc1(self):
        wb.open_new(r'https://youtu.be/KXXC0RQuJzo')

    def show_eleventhbiologyvideosc2(self):
        wb.open_new(r'https://youtu.be/Hm6fBcZ4g0o')

    def show_eleventhbiologyvideosc3(self):
        wb.open_new(r'https://youtu.be/HYMBOXhWHP0')

    def show_eleventhbiologyvideosc4(self):
        wb.open_new(r'https://youtu.be/qrNUPA0xaLY')

    def show_eleventhbiologyvideosc5(self):
        wb.open_new(r'https://youtu.be/Zrdn_xKESTA')

    def show_eleventhbiologyvideosc6(self):
        wb.open_new(r'https://youtu.be/5BTOr3AsliA')

    def show_eleventhbiologyvideosc7(self):
        wb.open_new(r'https://youtu.be/bXGPCb0kkso')

    def show_eleventhbiologyvideosc8(self):
        wb.open_new(r'https://youtu.be/8GM5ZQZlGb4')
    def show_twelthenglishvideosc1(self):
        wb.open_new(r'https://youtu.be/i_LTJ7uvBJw')

    def show_twelthenglishvideosc2(self):
        wb.open_new(r'https://youtu.be/Dkye2ZrNOe0')

    def show_twelthenglishvideosc3(self):
        wb.open_new(r'https://youtu.be/cjxohLxd4PE')

    def show_twelthenglishvideosc4(self):
        wb.open_new(r'https://youtu.be/4dSO73IFqP0')

    def show_twelthenglishvideosc5(self):
        wb.open_new(r'https://youtu.be/oaLZTUWjL0g')

    def show_twelthenglishvideosc6(self):
        wb.open_new(r'https://youtu.be/pvzA9YA7TDY')

    def show_twelthchemistryvideosc1(self):
        wb.open_new(r'https://youtu.be/r47ORPqhos8')

    def show_twelthchemistryvideosc2(self):
        wb.open_new(r'https://youtu.be/h1K1tQ6BW-s')

    def show_twelthchemistryvideosc3(self):
        wb.open_new(r'https://youtu.be/m0Uj7mSC6HU')

    def show_twelthchemistryvideosc4(self):
        wb.open_new(r'https://youtu.be/r4H5XjJPn58')

    def show_twelthchemistryvideosc5(self):
        wb.open_new(r'https://youtu.be/WIcb1WfJvJc')

    def show_twelthchemistryvideosc6(self):
        wb.open_new(r'https://youtu.be/3A1T13YkVx4')

    def show_twelthchemistryvideosc7(self):
        wb.open_new(r'https://youtu.be/TktHifwEusU')

    def show_twelthchemistryvideosc8(self):
        wb.open_new(r'https://youtu.be/OGD3q1eQ1TE')

    def show_twelthmathsvideosc1(self):
        wb.open_new(r'https://youtu.be/3ROzG6n4yMc')

    def show_twelthmathsvideosc2(self):
        wb.open_new(r'https://youtu.be/oDXx-cMsAJQ')

    def show_twelthmathsvideosc3(self):
        wb.open_new(r'https://youtu.be/DB4U-ici1DI')

    def show_twelthmathsvideosc4(self):
        wb.open_new(r'https://youtu.be/XDvSsDsLVLs')

    def show_twelthmathsvideosc5(self):
        wb.open_new(r'https://youtu.be/JAf_aSIJryg')

    def show_twelthmathsvideosc6(self):
        wb.open_new(r'https://youtu.be/Tk5zEk2xm9Y')

    def show_twelthphysicsvideosc1(self):
        wb.open_new(r'https://youtu.be/9242f4zMW60')

    def show_twelthphysicsvideosc2(self):
        wb.open_new(r'https://youtu.be/EkxHzAEGkp8')

    def show_twelthphysicsvideosc3(self):
        wb.open_new(r'https://youtu.be/1G_YX-z00ls')

    def show_twelthphysicsvideosc4(self):
        wb.open_new(r'https://youtu.be/XaglAjE7kHM')

    def show_twelthphysicsvideosc5(self):
        wb.open_new(r'https://youtu.be/xMlPfVvVnjw')

    def show_twelthphysicsvideosc6(self):
        wb.open_new(r'https://youtu.be/jBqv51buFQE')

    def show_twelthphysicsvideosc7(self):
        wb.open_new(r'https://youtu.be/NFCxEVomy4w')

    def show_twelthphysicsvideosc8(self):
        wb.open_new(r'https://youtu.be/FU6y1XIADdg')

    def show_twelthbiologyvideosc1(self):
        wb.open_new(r'https://youtu.be/6y13hYGPi8Q')

    def show_twelthbiologyvideosc2(self):
        wb.open_new(r'https://youtu.be/AoXCIKLmN2c')

    def show_twelthbiologyvideosc3(self):
        wb.open_new(r'https://youtu.be/Y8q5ztnd33E')

    def show_twelthbiologyvideosc4(self):
        wb.open_new(r'https://youtu.be/eFKtYb9CG_s')

    def show_twelthbiologyvideosc5(self):
        wb.open_new(r'https://youtu.be/OYeXMMwh3Lk')

    def show_twelthbiologyvideosc6(self):
        wb.open_new(r'https://youtu.be/gm4pZ_JXgRI')

    def show_twelthbiologyvideosc7(self):
        wb.open_new(r'https://youtu.be/itox8o_Ts94')

    def show_twelthbiologyvideosc8(self):
        wb.open_new(r'https://youtu.be/qEpQCF3mvoA')

    # assessment
    def show_prekgassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3ntixmaone8')

    def show_lkgassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3ntk4oaspgv')

    def show_ukgassess(self):
        wb.open(r'https://www.proprofs.com/quiz-school/story.php?title=ukg-assesment')

    def show_firstassess(self):
        wb.open(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3njiwoqskai')

    def show_secondassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3njuymgzcob')

    def show_thirdassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3nzmzmgisc1')

    def show_fourthassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3nzq1oa1m1g')

    def show_fifthassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3njixngbt4z')

    def show_sixthassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3njixngbt4z')

    def show_seventhassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3njqwmw20jz')

    def show_eighthassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=mjg3njq3mw4kpe')

    def show_ninthassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=1st-standard-assesment')

    def show_tenthassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=untitled-quiz_218960l')

    def show_eleventhassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=11th-assessment')

    def show_twelthassess(self):
        wb.open_new(r'https://www.proprofs.com/quiz-school/story.php?title=12th-assessment')

    # report
    def show_prekgass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3ntixmaone8&stat-shr-id=0d567e4d31f047d62e6a5d564f482314')

    def show_lkgass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3ntk4oaspgv&stat-shr-id=ea85b5c59d9d65cdb6482f15708506e7')

    def show_ukgass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=ukg-assesment&stat-shr-id=5d4fc49574033e81a55435c41d739145')

    def show_firstass(self):
        wb.open(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3njiwoqskai&stat-shr-id=cca4d06005b30abe77dca8a059eb402f')

    def show_secondass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3njuymgzcob&stat-shr-id=5f7a57892545d8cf43389c52a907e47f')

    def show_thirdass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3nzmzmgisc1&stat-shr-id=6bc6c742b30f7be858db1c102a0e0d37')

    def show_fourthass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3nzq1oa1m1g&stat-shr-id=e678f311a0d5235c91f29ddab6f652be')

    def show_fifthass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3njixngbt4z&stat-shr-id=59d353b47d6f74cedf658b954ad0d63e')

    def show_sixthass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3njm2mwdzg1&stat-shr-id=30664681069a0c636edf66aedffef761')

    def show_seventhass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3njqwmw20jz&stat-shr-id=8fedb7a0e91ceed8a67a6b68412dba78')

    def show_eighthass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=mjg3njq3mw4kpe&stat-shr-id=2f47733e6f2edeaf59d6ba9b8ab693ee')

    def show_ninthass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=1st-standard-assesment&stat-shr-id=422a28677a0b3b993f4a80ec7c570585')

    def show_tenthass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=untitled-quiz_218960l&stat-shr-id=8ee498c29ba195438129d39841f8fc23')

    def show_eleventhass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=11th-assessment&stat-shr-id=d6f4f30dff4188dc46923f3d9d085c24')

    def show_twelthass(self):
        wb.open_new(
            r'https://www.proprofs.com/quiz-school/stats.php?title=12th-assessment&stat-shr-id=ca878b1827c230b3c16b29cc4ee100b7')

    def show_helpmail(self):
        wb.open_new(
            r'https://www.google.com/search?q=gamil&rlz=1C1CHBF_enIN851IN851&oq=gamil&aqs=chrome..69i57j0l7.1557j0j15&sourceid=chrome&ie=UTF-8')


SmartTutorApp().run()
