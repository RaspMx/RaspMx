#! /usr.bin/python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import DMX
import numpy as np

class fenPrincipale(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        zoneCentrale = QMdiArea()

        menuConsole = self.menuBar().addMenu("&Console")
        actionVerrouiller = menuConsole.addAction("&Verrouiller la console")
        actionVerrouiller.setStatusTip("Verrouille la console par un mot de passe")
        actionRedemarrer = menuConsole.addAction(self.trUtf8("&Redémarrer"))
        actionRedemarrer.setStatusTip(self.trUtf8("Redémarre la console"))
        actionEteindre = menuConsole.addAction("&Eteindre")
        actionEteindre.setStatusTip("Eteint la console")
        menuTrame = self.menuBar().addMenu("&Trame")
        actionNTrame = menuTrame.addAction("&Nouvelle trame")
        actionNTrame.setStatusTip(self.trUtf8("Crée une nouvelle trame vierge"))
        actionNTrame.setShortcut(QKeySequence("Ctrl+N"))
        actionNFF = menuTrame.addAction("&Charger une trame depuis un fichier")
        actionNFF.setStatusTip(self.trUtf8("Charge une trame enregistrée"))
        actionNFF.setShortcut(QKeySequence("Ctrl+O"))
        actionRelire = menuTrame.addAction("&Relire la trame depuis son fichier")
        actionRelire.setStatusTip(self.trUtf8("Restore la trame actuelle à l'état de sa dernière sauvegarde"))
        actionRelire.setShortcut(QKeySequence("Ctrl+R"))
        actionSauver = menuTrame.addAction("&Sauvegarder la trame courante")
        actionSauver.setStatusTip("Sauve la trame actuelle")
        actionSauver.setShortcut(QKeySequence("Ctrl+S"))
        menuBus = self.menuBar().addMenu("&Bus DMX")
        actionEnvoyer = menuBus.addAction("&Envoyer la trame courante")
        actionEnvoyer.setStatusTip(self.trUtf8("Met à jour le bus avec la trame actuelle"))
        actionEnvoyer.setShortcut(QKeySequence("Ctrl+E"))
        actionRecevoir = menuBus.addAction(self.trUtf8("&Récupérer la trame actuelle du bus"))
        actionRecevoir.setStatusTip(self.trUtf8("Lit l'état du bus"))
        actionRecevoir.setShortcut(QKeySequence("Ctrl+B"))

        barreTrame = self.addToolBar("Trame")
        barreTrame.addAction(actionNTrame)
        barreTrame.addAction(actionSauver)
        barreTrame.addAction(actionEnvoyer)
        barreTrame.addSeparator()
        barreTrame.addAction(actionVerrouiller)
        barreTrame.addAction(actionEteindre)

        self.barreEtat = self.statusBar()
        labelBarrePret = QLabel()
        labelBarrePret.setText(self.trUtf8("Prêt"))
        self.barreEtat.addWidget(labelBarrePret)
        
        ongletManuel1 = QWidget()
        self.champMajCanal = QLineEdit()
        self.champMajCanal.setPlaceholderText(self.trUtf8("Canal à modifier"))
        self.champMajCanal.setInputMask("900")
        self.champMajValeur = QLineEdit()
        self.champMajValeur.setPlaceholderText("Nouvelle valeur pour le canal")
        self.champMajValeur.setInputMask("900")
        boutonMaj = QPushButton(self.trUtf8("Mettre à jour"))
        layoutMaj = QVBoxLayout()
        layoutMaj.addWidget(self.champMajCanal)
        layoutMaj.addWidget(self.champMajValeur)
        layoutMaj.addWidget(boutonMaj)
        self.champLireCanal = QLineEdit()
        self.champLireCanal.setPlaceholderText(self.trUtf8("Canal à lire"))
        boutonLire = QPushButton("Lire")
        self.champLireValeur = QLineEdit()
        self.champLireValeur.setPlaceholderText("Valeur lue")
        layoutLire = QVBoxLayout()
        layoutLire.addWidget(self.champLireCanal)
        layoutLire.addWidget(boutonLire)
        layoutLire.addWidget(self.champLireValeur)
        self.champRenommer = QLineEdit()
        self.champRenommer.setPlaceholderText("Renommer la trame courante")
        boutonRenommer = QPushButton("Renommer la trame courante")
        layoutRenommer = QVBoxLayout()
        layoutRenommer.addWidget(self.champRenommer)
        layoutRenommer.addWidget(boutonRenommer)
        self.labelContenuTrame = QLabel()
        self.labelContenuTrame.setText("Actualisez pour visualiser la trame")
        self.labelContenuTrame.setStyleSheet("background-color:black;color:violet")
        self.labelF1 = QLabel()
        self.labelF1.setText("F1")
        self.labelF1.setStyleSheet("background-color:red")
        self.labelF2 = QLabel()
        self.labelF2.setText("F2")
        self.labelF3 = QLabel()
        self.labelF3.setText("F3")
        self.labelF4 = QLabel()
        self.labelF4.setText("F4")
        self.labelF5 = QLabel()
        self.labelF5.setText("F5")
        self.labelF6 = QLabel()
        self.labelF6.setText("F6")
        self.labelF7 = QLabel()
        self.labelF7.setText("F7")
        self.labelF8 = QLabel()
        self.labelF8.setText("F8")
        self.labelF9 = QLabel()
        self.labelF9.setText("F9")
        self.labelF10 = QLabel()
        self.labelF10.setText("F10")
        self.labelF11 = QLabel()
        self.labelF11.setText("F11")
        self.labelF12 = QLabel()
        self.labelF12.setText("F12")
        layoutOnglet1 = QGridLayout()
        layoutOnglet1.addLayout(layoutMaj, 0,0,1,4)
        layoutOnglet1.addLayout(layoutLire, 0,4,1,4)
        layoutOnglet1.addLayout(layoutRenommer,0,8,1,4)
        layoutOnglet1.addWidget(self.labelContenuTrame, 1,0,16,12)
        layoutOnglet1.addWidget(self.labelF1,17,0)
        layoutOnglet1.addWidget(self.labelF2,17,1)
        layoutOnglet1.addWidget(self.labelF3,17,2)
        layoutOnglet1.addWidget(self.labelF4,17,3)
        layoutOnglet1.addWidget(self.labelF5,17,4)
        layoutOnglet1.addWidget(self.labelF6,17,5)
        layoutOnglet1.addWidget(self.labelF7,17,6)
        layoutOnglet1.addWidget(self.labelF8,17,7)
        layoutOnglet1.addWidget(self.labelF9,17,8)
        layoutOnglet1.addWidget(self.labelF10,17,9)
        layoutOnglet1.addWidget(self.labelF11,17,10)
        layoutOnglet1.addWidget(self.labelF12,17,11)
        ongletManuel1.setLayout(layoutOnglet1)
        
        ongletPupitre2 = QWidget()

        sousFenetre1 = zoneCentrale.addSubWindow(ongletManuel1)
        sousFenetre1.setWindowTitle(self.trUtf8("Edition de préparations"))
        sousFenetre2 = zoneCentrale.addSubWindow(ongletPupitre2)
        sousFenetre2.setWindowTitle("Mode pupitre")

        zoneCentrale.setViewMode(QMdiArea.TabbedView)

        self.setCentralWidget(zoneCentrale)

        scF1 = QShortcut(QKeySequence("F1"), self)
        scF2 = QShortcut(QKeySequence("F2"), self)
        scF3 = QShortcut(QKeySequence("F3"), self)
        scF4 = QShortcut(QKeySequence("F4"), self)
        scF5 = QShortcut(QKeySequence("F5"), self)
        scF6 = QShortcut(QKeySequence("F6"), self)
        scF7 = QShortcut(QKeySequence("F7"), self)
        scF8 = QShortcut(QKeySequence("F8"), self)
        scF9 = QShortcut(QKeySequence("F9"), self)
        scF10 = QShortcut(QKeySequence("F10"), self)
        scF11 = QShortcut(QKeySequence("F11"), self)
        scF12 = QShortcut(QKeySequence("F12"), self)
        
        self.majOk = 0
        self.TF1=DMX.Trame("F1", "F1")
        self.TF1.new()
        self.TF2=DMX.Trame("F2", "F2")
        self.TF2.new()
        self.TF3=DMX.Trame("F3", "F3")
        self.TF3.new()
        self.TF4=DMX.Trame("F4", "F4")
        self.TF4.new()
        self.TF5=DMX.Trame("F5", "F5")
        self.TF5.new()
        self.TF6=DMX.Trame("F6", "F6")
        self.TF6.new()
        self.TF7=DMX.Trame("F7", "F7")
        self.TF7.new()
        self.TF8=DMX.Trame("F8", "F8")
        self.TF8.new()
        self.TF9=DMX.Trame("F9", "F9")
        self.TF9.new()
        self.TF10=DMX.Trame("F10", "F10")
        self.TF10.new()
        self.TF11=DMX.Trame("F11", "F11")
        self.TF11.new()
        self.TF12=DMX.Trame("F12", "F12")
        self.TF12.new()
        print self.TF1.content
        self.trameCourante=self.TF1
        self.labelCourant = "label"+self.trameCourante.selecteur
        self.affichageContenuTrame()
        
        print self.trameCourante.selecteur
        print"'"
        print self.trameCourante.content

        self.setWindowTitle("Rasp'Mx - " + self.trameCourante.selecteur + " - " + self.trameCourante.name)
        
        self.connect(actionEteindre, SIGNAL("triggered()"), qApp, SLOT("quit()"))
        self.connect(boutonMaj, SIGNAL("clicked()"), self.maj)
        self.connect(boutonLire, SIGNAL("clicked()"), self.lire)
        self.connect(actionSauver, SIGNAL("triggered()"), self.enregistrerTrame)
        self.connect(boutonRenommer, SIGNAL("clicked()"), self.renommerTrame)
        self.connect(scF1, SIGNAL("activated()"), self.F1)
        self.connect(scF2, SIGNAL("activated()"), self.F2)
        self.connect(scF3, SIGNAL("activated()"), self.F3)
        self.connect(scF4, SIGNAL("activated()"), self.F4)
        self.connect(scF5, SIGNAL("activated()"), self.F5)
        self.connect(scF6, SIGNAL("activated()"), self.F6)
        self.connect(scF7, SIGNAL("activated()"), self.F7)
        self.connect(scF8, SIGNAL("activated()"), self.F8)
        self.connect(scF9, SIGNAL("activated()"), self.F9)
        self.connect(scF10, SIGNAL("activated()"), self.F10)
        self.connect(scF11, SIGNAL("activated()"), self.F11)
        self.connect(scF12, SIGNAL("activated()"), self.F12)
        
    def qsToString(self, qstring):
        return qstring.toInt()[0]
    
    def verifCanalMaj(self):
        print "Verif Canal !"
        if (self.qsToString(self.champMajCanal.text())<513):
            print "OK"
            self.majOk +=1
            
        else:
            print "Couillon!"
            self.barreEtat.showMessage(self.trUtf8("Le numéro du canal saisi n'est pas valide (il doit être compris entre 1 et 512)"), 5000)
            self.champMajCanal.setFocus()
            
    def verifValeurMaj(self):
        print "Verif Valeur !"
        if (self.qsToString(self.champMajValeur.text())<256):
            print "OK"
            self.majOk +=1
            
        else:
            print "Couillon!"
            self.barreEtat.showMessage(self.trUtf8("Le valeur saisie n'est pas valide (elle doit être comprise entre 0 et 255)"), 5000)
            self.champMajValeur.setFocus()

    def maj(self):
        self.verifValeurMaj()
        self.verifCanalMaj()
        print self.majOk
        if (self.majOk==2):
            print "La maj est possible"
            self.trameCourante.modif_canal(self.qsToString(self.champMajCanal.text()),
                               self.qsToString(self.champMajValeur.text()))
            self.barreEtat.showMessage(self.trUtf8("Mise à jour effectuée"))
            print "OK"
            print self.TF1.content
            self.majOk=0
            self.affichageContenuTrame()
        else:
            print "Je n'aurais jamais du voir ce message..."

    def lire(self):
        print "Lecture..."
        self.champLireValeur.setText(self.trameCourante.lire_canal(self.qsToString(self.champLireCanal.text())))
        print "OK"
        
    def enregistrerTrame(self):
        print "Enregistrement de la trame"
        messageConfirmation = QMessageBox(QMessageBox.Icon(),
                                          "Sauvegarde de la trame",
                                          self.trUtf8("La trame éxistante sera supprimée"),
                                          QMessageBox.Save|QMessageBox.Discard)
        res = messageConfirmation.exec_()
        print res
        if (res != 2048):
            self.barreEtat.showMessage("SAUVEGARDE NON EFFECTUEE !")
            return 0
        self.trameCourante.save(self.trameCourante.name)
        self.barreEtat.showMessage(self.trUtf8("Trame sauvegardée avec succès"))
        print "OK"
        
    def renommerTrame(self):
        print"Renommage de la trame"
        self.trameCourante.name=str(self.champRenommer.text())
        self.setWindowTitle("Rasp'Mx - " + self.trameCourante.selecteur + " - " + self.trameCourante.name)
        self.barreEtat.showMessage(self.trUtf8("Trame renommée"))
        print self.trameCourante.name

    def changeTrameCourante(self, nouvelleTrame, labelSelecteur):
        labelSelecteur.setStyleSheet("background-color:red")
        ancienneTrame = self.trameCourante.selecteur
        print ancienneTrame
        if (ancienneTrame == nouvelleTrame.selecteur):
            return 0
        if (ancienneTrame == "F1"):
            self.labelF1.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F2"):
            self.labelF2.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F3"):
            self.labelF3.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F4"):
            self.labelF4.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F5"):
            self.labelF5.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F6"):
            self.labelF6.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F7"):
            self.labelF7.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F8"):
            self.labelF8.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F9"):
            self.labelF9.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F10"):
            self.labelF10.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F11"):
            self.labelF11.setStyleSheet("background-color:transparent")
        elif (ancienneTrame == "F12"):
            self.labelF12.setStyleSheet("background-color:transparent")
        else:
            print "ERREUR ancienne trame"
            pass
        self.trameCourante = nouvelleTrame
        self.affichageContenuTrame()
        self.setWindowTitle("Rasp'Mx - " + self.trameCourante.selecteur + " - " + self.trameCourante.name)
        

    def F1(self):
        print "F1!"
        self.changeTrameCourante(self.TF1, self.labelF1)
              
    def F2(self):
        print "F2!"
        self.changeTrameCourante(self.TF2, self.labelF2)
              
    def F3(self):
        print "F3!"
        self.changeTrameCourante(self.TF3, self.labelF3)
              
    def F4(self):
        print "F4!"
        self.changeTrameCourante(self.TF4, self.labelF4)
              
    def F5(self):
        print "F5!"
        self.changeTrameCourante(self.TF5, self.labelF5)
              
    def F6(self):
        print "F6!"
        self.changeTrameCourante(self.TF6, self.labelF6)
              
    def F7(self):
        print "F7!"
        self.changeTrameCourante(self.TF7, self.labelF7)
              
    def F8(self):
        print "F8!"
        self.changeTrameCourante(self.TF8, self.labelF8)
              
    def F9(self):
        print "F9!"
        self.changeTrameCourante(self.TF9, self.labelF9)
              
    def F10(self):
        print "F10!"
        self.changeTrameCourante(self.TF10, self.labelF10)
              
    def F11(self):
        print "F11!"
        self.changeTrameCourante(self.TF11, self.labelF11)
              
    def F12(self):
        print "F12!"
        self.changeTrameCourante(self.TF12, self.labelF12)
        
    def affichageContenuTrame(self):
        contenu = np.zeros((1,513),int)
        for i in range(1,513):
            contenu[(0,i)] = self.trameCourante.lire_canal(i)

        affichage = "<table width=100% height=100%><tr>"
        j = 0
        for i in range(1,513):
            affichage += "<td>"+ str(i) + "<br /><b>" + str(contenu[(0,i)])+"</b></td>"
            if ((i/32)>j):
                affichage += "</tr><tr>"
                j+=1
        affichage+="</table>"
        self.labelContenuTrame.setText(affichage)    
