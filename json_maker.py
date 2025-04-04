import json
from collections import defaultdict
import re

html_text = """
 <option value="" selected>Alle Standorte</option>
                                                        <option value="19935">Altstadt</option>
                                                        <option value="19936">Dürrbach alle mit Hafen</option>
                                                        <option value="19937">Frauenland</option>
                                                        <option value="19938">Grombühl</option>
                                                        <option value="19939">Heidingsfeld</option>
                                                        <option value="403107">Heuchelhof aussen</option>
                                                        <option value="403108">Heuchelhof innen</option>
                                                        <option value="19941">Lengfeld</option>
                                                        <option value="19942">Lindleinsmühle</option>
                                                        <option value="403103">Mainviertel</option>
                                                        <option value="506176">Neumühle</option>
                                                        <option value="401083">Pilziggrund</option>
                                                        <option value="19940">Rottenbauer</option>
                                                        <option value="19943">Sanderau</option>
                                                        <option value="19944">Steinbachtal</option>
                                                        <option value="19945">Versbach</option>
                                                        <option value="19946">Zellerau</option>
                                                    </select>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td width="70%" height="26">Bitte Straße wählen</td>
                                                <td width="30%" align="right">
                                                    <select id="strlist" name="ev[str]">
                                                        <option value=""></option>
                                                        <option id="str_19950" value="19937">Abtsleitenweg</option>
                                                        <option id="str_19951" value="19943">Adalberostraße</option>
                                                        <option id="str_19952" value="19944">Adalbert-Stifter-Weg</option>
                                                        <option id="str_19953" value="19945">Adam-Güthlein-Straße</option>
                                                        <option id="str_19954" value="19946">Adelgundenweg</option>
                                                        <option id="str_505731" value="19937">Agnes-Sapper-Straße</option>
                                                        <option id="str_19955" value="19941">Ahornweg</option>
                                                        <option id="str_19956" value="19940">Akaziensteige</option>
                                                        <option id="str_19957" value="19937">Alandsgrund</option>
                                                        <option id="str_19958" value="19939">Albert-Balling-Gasse</option>
                                                        <option id="str_19959" value="19936">Albert-Einstein-Straße</option>
                                                        <option id="str_19960" value="19944">Albert-Günther-Weg</option>
                                                        <option id="str_19961" value="19937">Albert-Hoffa-Straße</option>
                                                        <option id="str_19962" value="19941">Albert-Schweitzer-Straße</option>
                                                        <option id="str_19963" value="19936">Albertsleitenweg</option>
                                                        <option id="str_19964" value="19942">Albertus-Magnus-Weg</option>
                                                        <option id="str_19965" value="19941">Alfons-M.-Mittnacht-Straße</option>
                                                        <option id="str_19966" value="19936">Alfred-Nobel-Straße</option>
                                                        <option id="str_19967" value="19939">Allendorfweg</option>
                                                        <option id="str_19968" value="19946">Allerseeweg</option>
                                                        <option id="str_505734" value="19937">Alte Fernstraße</option>
                                                        <option id="str_19969" value="403103">Alte Kasernstraße</option>
                                                        <option id="str_19970" value="19935">Alte Mainbrücke</option>
                                                        <option id="str_19972" value="19936">Alter Bergweg</option>
                                                        <option id="str_19971" value="19941">Alte Würzburger Straße</option>
                                                        <option id="str_20034" value="19943">Amalienstraße</option>
                                                        <option id="str_19973" value="19945">Am Altenberg</option>
                                                        <option id="str_505739" value="19937">Am Alten Flugfeld</option>
                                                        <option id="str_19974" value="19941">Am Bauhof</option>
                                                        <option id="str_19975" value="19940">Am Baumland</option>
                                                        <option id="str_19976" value="19944">Am Blosenberg</option>
                                                        <option id="str_19977" value="19935">Am Bruderhof</option>
                                                        <option id="str_403109" value="19940">Am Brunnen</option>
                                                        <option id="str_19978" value="19940">Am Brünnlein</option>
                                                        <option id="str_19979" value="403103">Am Dicken Turm</option>
                                                        <option id="str_19980" value="19936">Am Dürrbach</option>
                                                        <option id="str_19981" value="19945">Am Eselsbach</option>
                                                        <option id="str_19982" value="19943">Am Exerzierplatz</option>
                                                        <option id="str_19983" value="19940">Am Feldkreuz</option>
                                                        <option id="str_19984" value="19937">Am Galgenberg</option>
                                                        <option id="str_19985" value="19939">Am Geisberg</option>
                                                        <option id="str_19986" value="19936">Am Glitzelberg</option>
                                                        <option id="str_19987" value="19938">Am Greinberg</option>
                                                        <option id="str_19988" value="19941">Am Handelshof</option>
                                                        <option id="str_19989" value="19941">Am Hasensprung</option>
                                                        <option id="str_19990" value="19939">Am Heigelsbach</option>
                                                        <option id="str_19991" value="19940">Am Heuchel</option>
                                                        <option id="str_19992" value="19941">Am Hölzlein</option>
                                                        <option id="str_19993" value="19937">Am Hubland</option>
                                                        <option id="str_19994" value="19939">Am Hungrigen Bühl</option>
                                                        <option id="str_19995" value="19944">Am Kalkofen</option>
                                                        <option id="str_19996" value="19944">Am Klößberg</option>
                                                        <option id="str_19997" value="19937">Am Kugelfang</option>
                                                        <option id="str_19998" value="19936">Am Kuhberg</option>
                                                        <option id="str_19999" value="19941">Am Mühlenhang</option>
                                                        <option id="str_20000" value="19939">Am Nikolausspital</option>
                                                        <option id="str_20001" value="19939">Am Nikolaustor</option>
                                                        <option id="str_20002" value="19939">Am Ostbahnhof</option>
                                                        <option id="str_20003" value="19936">Am Pfaffenberg</option>
                                                        <option id="str_20004" value="403107">Am Pfaffenrain</option>
                                                        <option id="str_20005" value="19935">Am Pleidenturm</option>
                                                        <option id="str_20006" value="403107">Am Reuschert</option>
                                                        <option id="str_20007" value="19936">Am Roßberg</option>
                                                        <option id="str_20008" value="19939">Am Rubenland</option>
                                                        <option id="str_20009" value="19939">Am Salmannsturm</option>
                                                        <option id="str_20010" value="19936">Am Sand</option>
                                                        <option id="str_20011" value="19936">Am Schaftrieb</option>
                                                        <option id="str_20012" value="403107">Am Schellengraben</option>
                                                        <option id="str_20013" value="19936">Am Schenkenturm</option>
                                                        <option id="str_20014" value="19941">Am Schießgraben</option>
                                                        <option id="str_20015" value="19940">Am Schloß</option>
                                                        <option id="str_20016" value="19941">Am Schloßgarten</option>
                                                        <option id="str_20017" value="506176">Am Schwarzenberg</option>
                                                        <option id="str_20018" value="19945">Am Sonnenberg</option>
                                                        <option id="str_20019" value="19941">Am Sonnenhof</option>
                                                        <option id="str_20020" value="19941">Am Sonnfeld</option>
                                                        <option id="str_20021" value="19945">Am Stadtberg</option>
                                                        <option id="str_20022" value="19945">Am Steg</option>
                                                        <option id="str_20023" value="19938">Am Stein</option>
                                                        <option id="str_20024" value="19940">Am Stockbrunnen</option>
                                                        <option id="str_20026" value="401083">Am Stuck</option>
                                                        <option id="str_20027" value="19943">Am Studentenhaus</option>
                                                        <option id="str_505729" value="19937">Am Terrassenpark</option>
                                                        <option id="str_20028" value="401083">Am Trog</option>
                                                        <option id="str_20029" value="19944">Am Wald</option>
                                                        <option id="str_20030" value="19936">Am Wandberg</option>
                                                        <option id="str_20031" value="19941">Am Weinberg</option>
                                                        <option id="str_20032" value="19939">Am Westbahnhof</option>
                                                        <option id="str_20033" value="19945">Am Zehentfreien</option>
                                                        <option id="str_20035" value="19945">An den Breiten</option>
                                                        <option id="str_20036" value="19944">An den drei Pappeln</option>
                                                        <option id="str_20037" value="19936">An den Mühltannen</option>
                                                        <option id="str_20038" value="19936">An den Röthen</option>
                                                        <option id="str_20039" value="19939">An der Jahnhöhe</option>
                                                        <option id="str_20040" value="19945">An der Linde</option>
                                                        <option id="str_20041" value="19935">An der Löwenbrücke</option>
                                                        <option id="str_20042" value="19945">An der Pleichach</option>
                                                        <option id="str_20043" value="19939">An der Stadtmauer</option>
                                                        <option id="str_20044" value="19936">An der Steige</option>
                                                        <option id="str_20045" value="19937">An der Sternwarte</option>
                                                        <option id="str_20046" value="19939">Andreas-Grieser-Straße</option>
                                                        <option id="str_20047" value="19940">Anemonenweg</option>
                                                        <option id="str_20330" value="401083">Angermaierstraße</option>
                                                        <option id="str_20048" value="19944">Annaschlucht</option>
                                                        <option id="str_20049" value="19935">Annastraße</option>
                                                        <option id="str_20050" value="19944">Anne-Frank-Straße</option>
                                                        <option id="str_20051" value="19937">Anton-Bruckner-Straße</option>
                                                        <option id="str_20052" value="19946">Antonie-Werr-Straße</option>
                                                        <option id="str_20053" value="19939">Antonius-Lauck-Straße</option>
                                                        <option id="str_20054" value="19937">Armin-Knab-Straße</option>
                                                        <option id="str_20055" value="19943">Arndtstraße</option>
                                                        <option id="str_20056" value="19935">Artztlade</option>
                                                        <option id="str_505727" value="19937">Athanasius-Kircher-Straße</option>
                                                        <option id="str_20057" value="403107">Athener Ring</option>
                                                        <option id="str_20058" value="19941">Auf der Läng</option>
                                                        <option id="str_20059" value="19941">Auf der Röthe</option>
                                                        <option id="str_20060" value="19941">Auf der Schanz</option>
                                                        <option id="str_20061" value="19935">Augustinerstraße</option>
                                                        <option id="str_20062" value="19937">August-Sperl-Straße</option>
                                                        <option id="str_20063" value="19938">Äußere Aumühlstraße</option>
                                                        <option id="str_20064" value="19937">Äußerer Hublandweg</option>
                                                        <option id="str_20065" value="19937">Äußerer Neubergweg</option>
                                                        <option id="str_20066" value="19937">Äußerer Tränkeweg</option>
                                                        <option id="str_20067" value="19938">Auverastraße</option>
                                                        <option id="str_20068" value="19935">Bachgasse</option>
                                                        <option id="str_20069" value="19935">Badergasse</option>
                                                        <option id="str_20070" value="19935">Bahnhofplatz</option>
                                                        <option id="str_20071" value="19935">Bahnhofstraße</option>
                                                        <option id="str_20072" value="19935">Balthasar-Neumann-Promenade</option>
                                                        <option id="str_20073" value="19945">Banatstraße</option>
                                                        <option id="str_20074" value="19937">Barbarastraße</option>
                                                        <option id="str_20075" value="19935">Barbarossaplatz</option>
                                                        <option id="str_20076" value="19935">Bärengasse</option>
                                                        <option id="str_20077" value="19939">Bauernpfad</option>
                                                        <option id="str_20078" value="19936">Bauerstraße</option>
                                                        <option id="str_20079" value="19942">Bayernstraße</option>
                                                        <option id="str_20080" value="19935">Beethovenstraße</option>
                                                        <option id="str_20081" value="19937">Behrstraße</option>
                                                        <option id="str_20082" value="506176">Bei der Neumühle</option>
                                                        <option id="str_20083" value="19935">Beim Grafeneckart</option>
                                                        <option id="str_20084" value="403107">Belgrader Straße</option>
                                                        <option id="str_20085" value="19943">Bentheimstraße</option>
                                                        <option id="str_20086" value="19946">Benzstraße</option>
                                                        <option id="str_20087" value="19939">Berggasse</option>
                                                        <option id="str_20088" value="19935">Bergmeistergasse</option>
                                                        <option id="str_20089" value="19941">Bergstraße</option>
                                                        <option id="str_20090" value="19939">Berlichingenstraße</option>
                                                        <option id="str_20091" value="19935">Berliner Platz</option>
                                                        <option id="str_20092" value="403107">Berner Straße</option>
                                                        <option id="str_20093" value="19944">Betpfad</option>
                                                        <option id="str_20094" value="19935">Bibrastraße</option>
                                                        <option id="str_20095" value="19936">Birkenhain</option>
                                                        <option id="str_20096" value="19941">Birkenstraße</option>
                                                        <option id="str_20097" value="19935">Bismarckstraße</option>
                                                        <option id="str_20098" value="19935">Blasiusgasse</option>
                                                        <option id="str_20099" value="19935">Blöhlein</option>
                                                        <option id="str_20100" value="19939">Blosenbergpfad</option>
                                                        <option id="str_20101" value="19939">Blosenbergweg</option>
                                                        <option id="str_20102" value="19935">Bockgasse</option>
                                                        <option id="str_20103" value="19938">Bockspfad</option>
                                                        <option id="str_20104" value="19937">Bodelschwingstraße</option>
                                                        <option id="str_20105" value="19946">Bohlleitenweg</option>
                                                        <option id="str_20106" value="19935">Bohnesmühlgasse</option>
                                                        <option id="str_20107" value="19945">Bonhoefferstraße</option>
                                                        <option id="str_20108" value="403108">Bonner Straße</option>
                                                        <option id="str_20109" value="19938">Bossistraße</option>
                                                        <option id="str_20111" value="19945">Breite Länge</option>
                                                        <option id="str_20112" value="19939">Bremenweg</option>
                                                        <option id="str_20113" value="19943">Breslauer Straße</option>
                                                        <option id="str_20114" value="19937">Brettreichstraße</option>
                                                        <option id="str_20115" value="19940">Brombergweg</option>
                                                        <option id="str_20116" value="19935">Bronnbachergasse</option>
                                                        <option id="str_20117" value="19935">Bronnbacherhof</option>
                                                        <option id="str_20118" value="19938">Brücknerstraße</option>
                                                        <option id="str_20119" value="19945">Brunnenstraße</option>
                                                        <option id="str_20120" value="19945">Brunnfloßgasse</option>
                                                        <option id="str_20121" value="19946">Brunostraße</option>
                                                        <option id="str_20122" value="403108">Brüsseler Straße</option>
                                                        <option id="str_20123" value="19936">Buchengraben</option>
                                                        <option id="str_20124" value="19941">Buchenweg</option>
                                                        <option id="str_20125" value="403107">Budapester Straße</option>
                                                        <option id="str_20126" value="403107">Bukarester Straße</option>
                                                        <option id="str_20127" value="19939">Bürgermeister-Otto-Straße</option>
                                                        <option id="str_20128" value="403103">Burkarderstraße</option>
                                                        <option id="str_20129" value="19935">Büttnerstraße</option>
                                                        <option id="str_20130" value="19941">Carl-Orff-Straße</option>
                                                        <option id="str_20131" value="19937">Christelsteige</option>
                                                        <option id="str_20132" value="19944">Christoph-Mayer-Weg</option>
                                                        <option id="str_20133" value="19943">Conradistraße</option>
                                                        <option id="str_20134" value="19935">Crevennastraße</option>
                                                        <option id="str_20135" value="19937">Cronthalstraße</option>
                                                        <option id="str_20136" value="19946">Daimlerstraße</option>
                                                        <option id="str_20137" value="19937">Damaschkestraße</option>
                                                        <option id="str_20138" value="19943">Danziger Straße</option>
                                                        <option id="str_20139" value="403107">Delphiweg</option>
                                                        <option id="str_20140" value="403107">Delpstraße</option>
                                                        <option id="str_20141" value="403108">Den Haager Straße</option>
                                                        <option id="str_20142" value="19935">Dettelbachergasse</option>
                                                        <option id="str_20143" value="19946">Dieselstraße</option>
                                                        <option id="str_20144" value="19939">Dollgasse</option>
                                                        <option id="str_20145" value="19935">Domerpfarrgasse</option>
                                                        <option id="str_20146" value="19935">Domerschulstraße</option>
                                                        <option id="str_20147" value="19935">Dominikanergasse</option>
                                                        <option id="str_20148" value="19935">Dominikanerplatz</option>
                                                        <option id="str_20149" value="19935">Domstraße</option>
                                                        <option id="str_20150" value="19939">Domweg</option>
                                                        <option id="str_20151" value="19940">Dorfäcker</option>
                                                        <option id="str_20152" value="19941">Dorfgraben</option>
                                                        <option id="str_20153" value="19936">Dorfplatz</option>
                                                        <option id="str_20154" value="19939">Dornröschenweg</option>
                                                        <option id="str_20158" value="403103">Dreikronenstraße</option>
                                                        <option id="str_505726" value="19937">Dr.-Georg-Fuchs-Straße</option>
                                                        <option id="str_506072" value="19941">Dr.-Georg-Teichtweier-Straße</option>
                                                        <option id="str_20155" value="19941">Dr.-Heinrich-Wunderlich-Str.</option>
                                                        <option id="str_20159" value="403103">Dritte Felsengasse</option>
                                                        <option id="str_403122" value="403107">Dr.-Johanna-Stahl-Straße</option>
                                                        <option id="str_20156" value="19946">Dr.-Maria-Probst-Straße</option>
                                                        <option id="str_20157" value="19936">Dr.-Onymus-Straße</option>
                                                        <option id="str_20160" value="403107">Dubliner Straße</option>
                                                        <option id="str_20161" value="403107">Dundeestraße</option>
                                                        <option id="str_20162" value="19935">Dürerstraße</option>
                                                        <option id="str_20163" value="19936">Dürrbachtal</option>
                                                        <option id="str_20164" value="19939">Dürrenberg</option>
                                                        <option id="str_20165" value="19937">Ebertsklinge</option>
                                                        <option id="str_20166" value="19935">Ebrachergasse</option>
                                                        <option id="str_20167" value="19939">Eckleinsweg</option>
                                                        <option id="str_20168" value="19937">Edelstraße</option>
                                                        <option id="str_20169" value="403107">Edith-Stein-Straße</option>
                                                        <option id="str_20170" value="19936">Eduard-Buchner-Straße</option>
                                                        <option id="str_20171" value="19943">Egloffsteinstraße</option>
                                                        <option id="str_20172" value="19940">Eibelstadter Weg</option>
                                                        <option id="str_403111" value="19940">Eibenweg</option>
                                                        <option id="str_20173" value="19943">Eichendorffstraße</option>
                                                        <option id="str_403110" value="19940">Eichenweg</option>
                                                        <option id="str_20174" value="19935">Eichhornstraße</option>
                                                        <option id="str_20175" value="19935">Eichstraße</option>
                                                        <option id="str_20176" value="19939">Eisenbahnstraße</option>
                                                        <option id="str_20177" value="19946">Eiseneckstraße</option>
                                                        <option id="str_20178" value="19937">Eisenhoferstraße</option>
                                                        <option id="str_20179" value="19937">Eisenmannstraße</option>
                                                        <option id="str_20180" value="19935">Elefantengasse</option>
                                                        <option id="str_20181" value="19937">Elferweg</option>
                                                        <option id="str_505730" value="19937">Elisabeth-Scheuring-Straße</option>
                                                        <option id="str_20182" value="19936">Ellernweg</option>
                                                        <option id="str_20599" value="19939">Elli-Michler-Straße</option>
                                                        <option id="str_20183" value="403103">Elstergasse</option>
                                                        <option id="str_20184" value="19937">Emy-Roeder-Straße</option>
                                                        <option id="str_20185" value="19940">Engelsweg</option>
                                                        <option id="str_20186" value="19938">Enzelinstraße</option>
                                                        <option id="str_20187" value="403107">Ephesusweg</option>
                                                        <option id="str_20188" value="19941">Erlenweg</option>
                                                        <option id="str_20189" value="19938">Ernst-Reuter-Straße</option>
                                                        <option id="str_20190" value="19940">Ernst-Winter-Weg</option>
                                                        <option id="str_20191" value="403103">Erste Felsengasse</option>
                                                        <option id="str_20192" value="19946">Erster Siedlungsweg</option>
                                                        <option id="str_20193" value="19937">Erthalstraße</option>
                                                        <option id="str_20194" value="19937">Erzherzog-Karl-Platz</option>
                                                        <option id="str_20195" value="19940">Eschenweg</option>
                                                        <option id="str_20196" value="19941">Essiggarten</option>
                                                        <option id="str_20197" value="19945">Essigkrug</option>
                                                        <option id="str_20198" value="19945">Estenfelder Straße</option>
                                                        <option id="str_20199" value="19944">Eulensteige</option>
                                                        <option id="str_20200" value="19938">Europastern</option>
                                                        <option id="str_20201" value="19941">Falkenstraße</option>
                                                        <option id="str_20202" value="403107">Faribaultstraße</option>
                                                        <option id="str_20203" value="19941">Fasanenstraße</option>
                                                        <option id="str_20204" value="19946">Fasbenderstraße</option>
                                                        <option id="str_20205" value="19938">Faulenbergstraße</option>
                                                        <option id="str_20206" value="19943">Fechenbachstraße</option>
                                                        <option id="str_20207" value="19943">Feggrube</option>
                                                        <option id="str_20208" value="19943">Felix-Dahn-Straße</option>
                                                        <option id="str_20209" value="401083">Ferdinand-Nickles-Straße</option>
                                                        <option id="str_505732" value="19937">Ferdinand-Tietz-Straße</option>
                                                        <option id="str_20210" value="19937">Fichtestraße</option>
                                                        <option id="str_20211" value="19944">Finkenweg</option>
                                                        <option id="str_20212" value="19939">Fischleingasse</option>
                                                        <option id="str_20213" value="19943">Florastraße</option>
                                                        <option id="str_20214" value="19943">Floraweg</option>
                                                        <option id="str_20215" value="19941">Florian-Geyer-Straße</option>
                                                        <option id="str_20216" value="19941">Flürleinstraße</option>
                                                        <option id="str_20217" value="19941">Frankenlandstraße</option>
                                                        <option id="str_20218" value="19942">Frankenstraße 1-197 ung./2-210 ger. Nr.</option>
                                                        <option id="str_20219" value="19945">Frankenstraße 212-Ende ger./199-Ende ung. Nr.</option>
                                                        <option id="str_20220" value="19944">Frankenwarte</option>
                                                        <option id="str_20221" value="19946">Frankfurter Straße</option>
                                                        <option id="str_505728" value="19937">Franz-Brentano-Straße</option>
                                                        <option id="str_20222" value="19939">Franz-Bretz-Straße</option>
                                                        <option id="str_20223" value="19946">Franz-Horn-Straße</option>
                                                        <option id="str_20224" value="19935">Franziskanergasse</option>
                                                        <option id="str_20225" value="19935">Franziskanerplatz</option>
                                                        <option id="str_20226" value="19937">Franz-Liszt-Straße</option>
                                                        <option id="str_20227" value="19943">Franz-Ludwig-Straße</option>
                                                        <option id="str_20228" value="19944">Franzosenweg</option>
                                                        <option id="str_20229" value="19937">Franz-Schubert-Straße</option>
                                                        <option id="str_20230" value="19937">Franz-Stadelmayer-Straße</option>
                                                        <option id="str_20231" value="19937">Frauenlandplatz</option>
                                                        <option id="str_20232" value="19937">Frauenlandstraße</option>
                                                        <option id="str_20233" value="19939">Frau-Holle-Weg</option>
                                                        <option id="str_20234" value="19938">Fraunhoferstraße</option>
                                                        <option id="str_20235" value="19943">Friedenstraße</option>
                                                        <option id="str_20236" value="19940">Friedhofstraße</option>
                                                        <option id="str_20237" value="19938">Friedrich-Bergius-Ring</option>
                                                        <option id="str_20238" value="19935">Friedrich-Ebert-Ring 1-12</option>
                                                        <option id="str_20239" value="19943">Friedrich-Ebert-Ring ab 13</option>
                                                        <option id="str_20240" value="19937">Friedrich-Fick-Straße</option>
                                                        <option id="str_20241" value="19936">Friedrich-Koenig-Straße</option>
                                                        <option id="str_20242" value="19936">Friedrich-Kohlrausch-Straße</option>
                                                        <option id="str_20243" value="19943">Friedrich-Spee-Straße</option>
                                                        <option id="str_20244" value="19946">Friedrichstraße</option>
                                                        <option id="str_20245" value="19937">Friesstraße</option>
                                                        <option id="str_20246" value="19941">Fritz-Erler-Straße</option>
                                                        <option id="str_20247" value="19936">Fritz-Haber-Straße</option>
                                                        <option id="str_20248" value="19937">Fröbelstraße</option>
                                                        <option id="str_20249" value="19946">Fröhlichstraße</option>
                                                        <option id="str_20250" value="19941">Frühlingstraße</option>
                                                        <option id="str_20251" value="19939">Fuchsgasse</option>
                                                        <option id="str_20252" value="19938">Füchsleinstraße</option>
                                                        <option id="str_20253" value="19938">Gabelsbergerstraße</option>
                                                        <option id="str_20254" value="19936">Gadheimer Straße</option>
                                                        <option id="str_20255" value="19946">Gänsleinsweg</option>
                                                        <option id="str_20256" value="19943">Gartenstraße</option>
                                                        <option id="str_20257" value="19938">Gattingerstraße</option>
                                                        <option id="str_20258" value="19945">Gebr.-Grimm-Straße</option>
                                                        <option id="str_20259" value="19937">Gegenbaurstraße</option>
                                                        <option id="str_20260" value="19943">Geibelstraße</option>
                                                        <option id="str_20261" value="19939">Geisberg</option>
                                                        <option id="str_20262" value="19939">Geisberggraben</option>
                                                        <option id="str_20263" value="19938">Georg-Böhm-Straße</option>
                                                        <option id="str_20264" value="19941">Georg-Engel-Straße</option>
                                                        <option id="str_20265" value="19946">Georg-Eydel-Straße</option>
                                                        <option id="str_20266" value="19937">Georg-Sittig-Straße</option>
                                                        <option id="str_20267" value="19935">Gerberstraße</option>
                                                        <option id="str_20268" value="19937">Gerbrunner Weg</option>
                                                        <option id="str_505735" value="19937">Gerda-Laufer-Straße</option>
                                                        <option id="str_20269" value="19935">Gertraudgasse</option>
                                                        <option id="str_20270" value="19944">Gertraud-Rostosky-Straße</option>
                                                        <option id="str_20271" value="19937">Gertrud-von-le-Fort-Straße</option>
                                                        <option id="str_20272" value="19935">Geschwister-Scholl-Platz</option>
                                                        <option id="str_20273" value="403107">Giebelstädter Steige</option>
                                                        <option id="str_20274" value="19939">Glacisweg</option>
                                                        <option id="str_20275" value="19935">Glockengasse</option>
                                                        <option id="str_20276" value="19937">Gneisenaustraße</option>
                                                        <option id="str_20277" value="19937">Göbelslehenstraße</option>
                                                        <option id="str_20278" value="403107">Goerdelerstraße</option>
                                                        <option id="str_20279" value="19935">Goethestraße</option>
                                                        <option id="str_20280" value="19945">Goldbergstraße</option>
                                                        <option id="str_20281" value="19946">Gosbertsteige</option>
                                                        <option id="str_20282" value="19935">Gotengasse</option>
                                                        <option id="str_20283" value="19935">Grabenberg</option>
                                                        <option id="str_20284" value="19935">Grabengasse</option>
                                                        <option id="str_20285" value="19943">Graf-Luckner-Weiher</option>
                                                        <option id="str_20286" value="19937">Grasweg</option>
                                                        <option id="str_20287" value="19943">Greiffenclaustraße</option>
                                                        <option id="str_20288" value="19937">Greisingstraße</option>
                                                        <option id="str_20289" value="19935">Gressengasse</option>
                                                        <option id="str_20290" value="19945">Griesäckerstraße</option>
                                                        <option id="str_20291" value="19943">Grillparzerstraße</option>
                                                        <option id="str_20292" value="19938">Grombühlstraße</option>
                                                        <option id="str_20293" value="19936">Grundäckerstraße</option>
                                                        <option id="str_20294" value="19935">Grünewaldstraße</option>
                                                        <option id="str_20295" value="19944">Guggelesgraben</option>
                                                        <option id="str_20296" value="19946">Gulbranssonstraße</option>
                                                        <option id="str_20297" value="19938">Gutenbergstraße</option>
                                                        <option id="str_20298" value="19937">Gutental</option>
                                                        <option id="str_20299" value="19936">Güterbahnhof Zell</option>
                                                        <option id="str_20300" value="19944">Guttenbergerstraße</option>
                                                        <option id="str_20301" value="19946">Haafstraße</option>
                                                        <option id="str_20302" value="19937">Hackstetterstraße</option>
                                                        <option id="str_20303" value="19935">Häfnergasse</option>
                                                        <option id="str_20304" value="19935">Hahnenhof</option>
                                                        <option id="str_20305" value="19937">Händelstraße</option>
                                                        <option id="str_20306" value="19935">Handgasse</option>
                                                        <option id="str_20307" value="19938">Hans-Brandmann-Weg</option>
                                                        <option id="str_20308" value="19937">Hans-Löffler-Straße</option>
                                                        <option id="str_20309" value="19944">Hans-Sachs-Weg</option>
                                                        <option id="str_20310" value="19935">Harfenstraße</option>
                                                        <option id="str_20311" value="19946">Hartmannstraße</option>
                                                        <option id="str_20312" value="19935">Haugerglacisstraße</option>
                                                        <option id="str_20313" value="19935">Haugerkirchgasse</option>
                                                        <option id="str_20314" value="19935">Haugerkirchplatz</option>
                                                        <option id="str_20315" value="19935">Haugerpfarrgasse</option>
                                                        <option id="str_20316" value="19935">Haugerring</option>
                                                        <option id="str_20317" value="19938">Häuselsberg</option>
                                                        <option id="str_20318" value="19937">Haydnstraße</option>
                                                        <option id="str_20319" value="19943">Hebbelstraße</option>
                                                        <option id="str_20320" value="19939">Hedanstraße</option>
                                                        <option id="str_20321" value="19945">Heide</option>
                                                        <option id="str_20322" value="403107">Heidingsfelder Weg</option>
                                                        <option id="str_20323" value="19937">Heimgartenweg</option>
                                                        <option id="str_20325" value="19935">Heinestraße</option>
                                                        <option id="str_20326" value="19936">Heinrichsleitenweg</option>
                                                        <option id="str_20327" value="19944">Heinrich-Zeuner-Straße</option>
                                                        <option id="str_20328" value="19941">Heisenbergstraße</option>
                                                        <option id="str_20329" value="19944">Heißberg</option>
                                                        <option id="str_20331" value="403107">Helsinkistraße</option>
                                                        <option id="str_20332" value="19937">Henlestraße</option>
                                                        <option id="str_20333" value="19939">Heriedenweg</option>
                                                        <option id="str_20334" value="19944">Hermann-Löns-Weg</option>
                                                        <option id="str_20335" value="19941">Hermann-Mitnacht-Straße</option>
                                                        <option id="str_20336" value="19937">Hermann-Schell-Straße</option>
                                                        <option id="str_20338" value="19941">Hermann-Zürrlein-Str.</option>
                                                        <option id="str_20339" value="19941">Herrnhofstraße</option>
                                                        <option id="str_20340" value="19935">Herrnstraße</option>
                                                        <option id="str_20341" value="19939">Herta-Mannheimer-Weg</option>
                                                        <option id="str_20342" value="19938">Hertzstraße</option>
                                                        <option id="str_20343" value="19935">Herzogenstraße</option>
                                                        <option id="str_20344" value="19942">Hessenstraße</option>
                                                        <option id="str_20345" value="403107">Heuchelhofstraße</option>
                                                        <option id="str_20346" value="19946">Hexenbruchweg</option>
                                                        <option id="str_20347" value="19940">Hintere Heuchel</option>
                                                        <option id="str_20348" value="19945">Hintere Kirchgasse</option>
                                                        <option id="str_20349" value="19944">Hinterer Johannishof</option>
                                                        <option id="str_20350" value="19939">Hinterer Kirchbergweg</option>
                                                        <option id="str_20351" value="19945">Hinterer Kühlenberg</option>
                                                        <option id="str_20352" value="19944">Hinteres Steinbachtal</option>
                                                        <option id="str_20353" value="19943">Hirschberger Straße</option>
                                                        <option id="str_20354" value="19936">Hirschleinstraße</option>
                                                        <option id="str_20355" value="19946">Höchberger Straße</option>
                                                        <option id="str_20356" value="19940">Hoffeldäcker</option>
                                                        <option id="str_20357" value="19936">Hofleitenweg</option>
                                                        <option id="str_20358" value="19939">Hofmannstraße</option>
                                                        <option id="str_20359" value="19937">Hofmeierstraße</option>
                                                        <option id="str_20360" value="19935">Hofstallstraße</option>
                                                        <option id="str_20361" value="19935">Hofstraße</option>
                                                        <option id="str_20363" value="19944">Hoher Weg</option>
                                                        <option id="str_20362" value="403107">Hohe Steige</option>
                                                        <option id="str_20364" value="19940">Holunderweg</option>
                                                        <option id="str_20365" value="19937">Holzbühlweg</option>
                                                        <option id="str_20366" value="19938">Hölzlesweg</option>
                                                        <option id="str_20367" value="19935">Holztorgasse</option>
                                                        <option id="str_20368" value="19939">Holzweg</option>
                                                        <option id="str_20369" value="19936">Hopfenberg</option>
                                                        <option id="str_20370" value="19935">Hörleingasse</option>
                                                        <option id="str_20371" value="403107">Huberstraße</option>
                                                        <option id="str_20372" value="19937">Hubertistraße</option>
                                                        <option id="str_20373" value="19944">Hubertusschlucht</option>
                                                        <option id="str_20374" value="19944">Hubertusweg</option>
                                                        <option id="str_505725" value="19937">Hublandplatz</option>
                                                        <option id="str_20375" value="19935">Huebergasse</option>
                                                        <option id="str_20376" value="19939">Hunsingerweg</option>
                                                        <option id="str_20377" value="19935">Husarenstraße</option>
                                                        <option id="str_20378" value="19943">Huttenstraße</option>
                                                        <option id="str_20379" value="19936">Hüttenweg</option>
                                                        <option id="str_506025" value="19937">Ilse-Totzke-Straße</option>
                                                        <option id="str_20380" value="19936">Im Grund</option>
                                                        <option id="str_20381" value="19936">Im Hirschlein</option>
                                                        <option id="str_20382" value="19937">Im Hubland</option>
                                                        <option id="str_20383" value="19938">Im Kreuz</option>
                                                        <option id="str_20384" value="19941">Industriestraße</option>
                                                        <option id="str_20385" value="19935">Ingolstadter Hof</option>
                                                        <option id="str_20386" value="19938">Innere Aumühlstraße</option>
                                                        <option id="str_20387" value="19935">Innerer Graben</option>
                                                        <option id="str_20388" value="19937">Innerer Hublandweg</option>
                                                        <option id="str_20389" value="19941">Jägerruh</option>
                                                        <option id="str_20390" value="19946">Jägerstraße</option>
                                                        <option id="str_20391" value="19941">Jahnstraße</option>
                                                        <option id="str_20392" value="19937">Jakob-Riedinger-Straße</option>
                                                        <option id="str_20393" value="19937">Johannes-Kepler-Straße</option>
                                                        <option id="str_20394" value="19945">Johann-Herrmann-Straße</option>
                                                        <option id="str_20395" value="19944">Johannisweg</option>
                                                        <option id="str_20396" value="19935">Johanniterplatz</option>
                                                        <option id="str_20397" value="19941">Johanniterweg</option>
                                                        <option id="str_20398" value="19936">Johann-Salomon-Straße</option>
                                                        <option id="str_20399" value="19935">Johann-Sperl-Straße</option>
                                                        <option id="str_505736" value="19937">John-Skilton-Straße</option>
                                                        <option id="str_20400" value="19938">Josefplatz</option>
                                                        <option id="str_20401" value="19938">Josef-Schneider-Straße</option>
                                                        <option id="str_20402" value="19935">Josef-Stangel-Platz</option>
                                                        <option id="str_20403" value="19938">Josefstraße</option>
                                                        <option id="str_20404" value="401083">Joseph-Seitz-Straße</option>
                                                        <option id="str_20405" value="19944">Judenbühlweg</option>
                                                        <option id="str_20406" value="19939">Judenhof</option>
                                                        <option id="str_20407" value="19939">Judenplan</option>
                                                        <option id="str_20408" value="19939">Julius-Echter-Straße</option>
                                                        <option id="str_20409" value="19935">Juliuspromenade</option>
                                                        <option id="str_20410" value="19935">Kaiserplatz</option>
                                                        <option id="str_20411" value="19935">Kaiserstraße</option>
                                                        <option id="str_20412" value="19937">Kantstraße</option>
                                                        <option id="str_20413" value="19944">Käppele</option>
                                                        <option id="str_20414" value="19935">Kapuzinerstraße</option>
                                                        <option id="str_20415" value="19935">Kardinal-Döpfner-Platz</option>
                                                        <option id="str_20416" value="19935">Kardinal-Faulhaber-Platz</option>
                                                        <option id="str_20417" value="19936">Karl-Ferdinant-Braun-Straße</option>
                                                        <option id="str_20418" value="19944">Karl-Pfetscher-Weg</option>
                                                        <option id="str_20419" value="19937">Karl-Ritter-von-Frisch-Weg</option>
                                                        <option id="str_20420" value="19939">Karl-Straub-Straße</option>
                                                        <option id="str_20421" value="19935">Karmelitenstraße</option>
                                                        <option id="str_20422" value="19935">Kärrnergasse</option>
                                                        <option id="str_20423" value="19935">Kartause</option>
                                                        <option id="str_20424" value="19940">Kastanienstraße</option>
                                                        <option id="str_20425" value="19935">Katharinengasse</option>
                                                        <option id="str_20426" value="403103">Katzengasse</option>
                                                        <option id="str_20427" value="19939">Kaulstraße</option>
                                                        <option id="str_20428" value="19937">Keesburgstraße</option>
                                                        <option id="str_20430" value="19941">Keltenstraße</option>
                                                        <option id="str_20431" value="19937">Kettelerstraße</option>
                                                        <option id="str_20432" value="19935">Kettengasse</option>
                                                        <option id="str_20433" value="19940">Kiefernweg</option>
                                                        <option id="str_20434" value="19939">Kieseläckerweg</option>
                                                        <option id="str_20435" value="19935">Kiliansplatz</option>
                                                        <option id="str_20436" value="19937">Kirchbühlstraße</option>
                                                        <option id="str_20437" value="19939">Kirchgasse</option>
                                                        <option id="str_20438" value="19939">Kirchhofstraße</option>
                                                        <option id="str_20439" value="19939">Kirchplatz</option>
                                                        <option id="str_403112" value="19940">Kirschbaumweg</option>
                                                        <option id="str_20440" value="19937">Kittelstraße</option>
                                                        <option id="str_20441" value="19944">Klara-Löwe-Straße</option>
                                                        <option id="str_403113" value="19940">Kleines Flürlein</option>
                                                        <option id="str_20442" value="19943">Kleiststraße</option>
                                                        <option id="str_20443" value="19944">Kleßbergsteige</option>
                                                        <option id="str_20444" value="19935">Kliebertstraße</option>
                                                        <option id="str_20445" value="19939">Klingenstraße</option>
                                                        <option id="str_20446" value="19936">Klingenweg</option>
                                                        <option id="str_20447" value="19935">Klinikstraße</option>
                                                        <option id="str_20448" value="19939">Klopfergasse</option>
                                                        <option id="str_20449" value="19935">Klostergasse</option>
                                                        <option id="str_20450" value="19939">Klosterstraße</option>
                                                        <option id="str_20451" value="19944">Kniebreche</option>
                                                        <option id="str_20452" value="19939">Köchleinsweg</option>
                                                        <option id="str_20453" value="19935">Koellikerstraße</option>
                                                        <option id="str_20454" value="19935">Kohlenhofstraße</option>
                                                        <option id="str_20455" value="19939">Kolonieweg</option>
                                                        <option id="str_20456" value="19935">Kolpingstraße</option>
                                                        <option id="str_20457" value="19944">König-Heinrich-Straße</option>
                                                        <option id="str_20458" value="19943">Königsberger Straße</option>
                                                        <option id="str_20459" value="19935">Konradstraße</option>
                                                        <option id="str_20462" value="403107">Kopenhagener Straße</option>
                                                        <option id="str_20460" value="19936">Koppberggraben</option>
                                                        <option id="str_20461" value="19936">Koppbergweg</option>
                                                        <option id="str_20463" value="19935">Korngasse</option>
                                                        <option id="str_20464" value="19935">Kranenkai</option>
                                                        <option id="str_20465" value="19936">Krautäckerstraße</option>
                                                        <option id="str_20466" value="19936">Kreuzbergstraße</option>
                                                        <option id="str_20467" value="19935">Kroatengasse</option>
                                                        <option id="str_20468" value="19945">Kronbergstraße</option>
                                                        <option id="str_20469" value="19945">Kühlenbergstraße</option>
                                                        <option id="str_20470" value="19941">Kürnachtalstraße</option>
                                                        <option id="str_20471" value="19935">Kürschner Hof</option>
                                                        <option id="str_20472" value="19941">Kurze Gasse</option>
                                                        <option id="str_505740" value="19937">Landsteinerstraße</option>
                                                        <option id="str_20473" value="19935">Landwehrstraße</option>
                                                        <option id="str_20474" value="19937">Lange Bögen</option>
                                                        <option id="str_20475" value="19936">Langer Weg</option>
                                                        <option id="str_20476" value="19945">Langes Gräthlein</option>
                                                        <option id="str_20477" value="19935">Langgasse</option>
                                                        <option id="str_20478" value="19940">Lärchenweg</option>
                                                        <option id="str_20479" value="403103">Laufergasse</option>
                                                        <option id="str_20480" value="19941">Laurentiusstraße</option>
                                                        <option id="str_20481" value="19939">Lehmgrubenweg</option>
                                                        <option id="str_20482" value="19937">Lehnleitenweg</option>
                                                        <option id="str_20483" value="19935">Leiblstraße</option>
                                                        <option id="str_505737" value="19937">Leightonstraße</option>
                                                        <option id="str_20484" value="19944">Leistenstraße</option>
                                                        <option id="str_20485" value="19939">Leitenäckerweg</option>
                                                        <option id="str_20486" value="19939">Leitengraben</option>
                                                        <option id="str_20487" value="19944">Leitenpfad</option>
                                                        <option id="str_20488" value="19937">Lendnerstraße</option>
                                                        <option id="str_404556" value="19941">Lengfelder Höh</option>
                                                        <option id="str_506723" value="19941">Lengfelder Landwehr</option>
                                                        <option id="str_20489" value="19945">Lengfelder Straße</option>
                                                        <option id="str_20490" value="19946">Leonhard-Frank-Promenade</option>
                                                        <option id="str_20491" value="19937">Leo-Weismantel-Straße</option>
                                                        <option id="str_20492" value="19937">Lerchenhain</option>
                                                        <option id="str_20493" value="19937">Lerchenweg</option>
                                                        <option id="str_20494" value="19943">Lessingstraße</option>
                                                        <option id="str_20495" value="19937">Leubestraße</option>
                                                        <option id="str_20496" value="403107">Leuschnerstraße</option>
                                                        <option id="str_20497" value="19944">Leutfresserweg</option>
                                                        <option id="str_20498" value="19941">Liborius-Wagner-Straße</option>
                                                        <option id="str_20499" value="19936">Liebigstraße</option>
                                                        <option id="str_20500" value="19943">Liegnitzer Straße</option>
                                                        <option id="str_20501" value="19940">Lilienweg</option>
                                                        <option id="str_20502" value="19938">Lindachfeldweg</option>
                                                        <option id="str_20503" value="19935">Lindahlstraße</option>
                                                        <option id="str_20504" value="19940">Lindenstraße</option>
                                                        <option id="str_20505" value="19940">Lindflurer Straße</option>
                                                        <option id="str_20506" value="19938">Lindleinstraße</option>
                                                        <option id="str_20507" value="19938">Lindleshang</option>
                                                        <option id="str_403114" value="19940">Linsen</option>
                                                        <option id="str_20508" value="403107">Lissabonner Straße</option>
                                                        <option id="str_20509" value="19939">Löffelgasse</option>
                                                        <option id="str_20510" value="403107">Londoner Straße</option>
                                                        <option id="str_20511" value="19937">Lortzingstraße</option>
                                                        <option id="str_506715" value="19936">Lothar-Forster-Straße</option>
                                                        <option id="str_20512" value="19938">Louis-Pasteur-Straße</option>
                                                        <option id="str_20513" value="19943">Ludwigkai</option>
                                                        <option id="str_20514" value="19935">Ludwigstraße</option>
                                                        <option id="str_20515" value="19946">Ludwig-Weis-Straße</option>
                                                        <option id="str_20516" value="19936">Luitpoldgraben</option>
                                                        <option id="str_20517" value="19936">Luitpoldquelle</option>
                                                        <option id="str_20518" value="19946">Luitpoldstraße</option>
                                                        <option id="str_20519" value="403108">Luxemburger Straße</option>
                                                        <option id="str_20520" value="19944">Maasweg</option>
                                                        <option id="str_20521" value="403107">Madrider Ring</option>
                                                        <option id="str_505741" value="19937">Magdalena-Schoch-Straße</option>
                                                        <option id="str_403115" value="19940">Mageritenweg</option>
                                                        <option id="str_20522" value="19945">Maidbronner Weg</option>
                                                        <option id="str_20523" value="19935">Maiergasse</option>
                                                        <option id="str_20524" value="19946">Maillingerstraße</option>
                                                        <option id="str_20525" value="19946">Mainaustraße</option>
                                                        <option id="str_20526" value="19937">Maingäßchen</option>
                                                        <option id="str_20527" value="19939">Maingasse</option>
                                                        <option id="str_20528" value="19935">Mainkai</option>
                                                        <option id="str_20529" value="19944">Mainleitenweg</option>
                                                        <option id="str_20530" value="19941">Malterserweg</option>
                                                        <option id="str_20531" value="19940">Mandelbaumweg</option>
                                                        <option id="str_20532" value="19935">Marcusstraße</option>
                                                        <option id="str_20533" value="19937">Marianhillstraße</option>
                                                        <option id="str_20534" value="19944">Maria-Theresia-Promenade</option>
                                                        <option id="str_20535" value="19946">Marienberg</option>
                                                        <option id="str_20536" value="19935">Marienplatz</option>
                                                        <option id="str_20537" value="19935">Marienstraße</option>
                                                        <option id="str_20538" value="19935">Marktgasse</option>
                                                        <option id="str_20539" value="19935">Marktplatz</option>
                                                        <option id="str_20540" value="19935">Martin-Luther-Straße</option>
                                                        <option id="str_20541" value="19935">Martinstraße</option>
                                                        <option id="str_20542" value="19938">Matterstockstraße</option>
                                                        <option id="str_20543" value="19937">Matthias-Ehrenfried-Straße</option>
                                                        <option id="str_20544" value="19939">Matthias-Noell-Weg</option>
                                                        <option id="str_20545" value="19935">Maulhardgasse</option>
                                                        <option id="str_20546" value="19937">Maurmeierstraße</option>
                                                        <option id="str_20547" value="19936">Max-Born-Straße</option>
                                                        <option id="str_20548" value="19943">Max-Dauthendey-Straße</option>
                                                        <option id="str_20549" value="19937">Max-Heim-Straße</option>
                                                        <option id="str_403116" value="19940">Maximilian-Kolbe-Strasse</option>
                                                        <option id="str_506006" value="403107">Max-Mengeringhausen-Straße</option>
                                                        <option id="str_20551" value="19946">Max-Planck-Straße</option>
                                                        <option id="str_20552" value="19937">Max-Reger-Straße</option>
                                                        <option id="str_20553" value="19939">Max-Schnabel-Straße</option>
                                                        <option id="str_20554" value="19935">Maxstraße</option>
                                                        <option id="str_20555" value="19936">Max-von-Laue-Straße</option>
                                                        <option id="str_20556" value="19944">Meisenweg</option>
                                                        <option id="str_20558" value="19944">Mergentheimer Straße 1-21 ung./4-110 ger. Nr.</option>
                                                        <option id="str_20557" value="19939">Mergentheimer Straße  23-Ende ung./112-Ende ger. Nr.</option>
                                                        <option id="str_20559" value="19937">Methfesselstraße</option>
                                                        <option id="str_20560" value="19937">Meyer-Olbersleben-Straße</option>
                                                        <option id="str_20561" value="19945">Michael-Brand-Straße</option>
                                                        <option id="str_20562" value="19946">Michelstraße</option>
                                                        <option id="str_20563" value="403107">Miletweg</option>
                                                        <option id="str_20324" value="19943">Milly-Marbe-Fries-Weg</option>
                                                        <option id="str_20564" value="19945">Mittlere Heerbergstraße</option>
                                                        <option id="str_20565" value="19944">Mittlerer Dallenbergweg</option>
                                                        <option id="str_20566" value="19938">Mittlerer Greinbergweg</option>
                                                        <option id="str_20567" value="19939">Mittlerer Katzenbergweg</option>
                                                        <option id="str_20568" value="19939">Mittlerer Kirchbergweg</option>
                                                        <option id="str_20569" value="19937">Mittlerer Neubergweg</option>
                                                        <option id="str_20570" value="19938">Mittlerer Schalksbergweg</option>
                                                        <option id="str_20571" value="19944">Mittlerer Steinbachweg</option>
                                                        <option id="str_20572" value="19938">Mittlerer Steinbergweg</option>
                                                        <option id="str_20573" value="19936">Mittlerer Wiesenweg</option>
                                                        <option id="str_20574" value="19936">Mohnstraße</option>
                                                        <option id="str_20575" value="19946">Moltkestraße</option>
                                                        <option id="str_20576" value="19937">Mönchbergstraße</option>
                                                        <option id="str_20577" value="19939">Mönchsgartenweg</option>
                                                        <option id="str_20578" value="19938">Morellistraße</option>
                                                        <option id="str_20579" value="19935">Moritzgasse</option>
                                                        <option id="str_20580" value="19946">Moscheeweg</option>
                                                        <option id="str_20581" value="403107">Moskauer Ring</option>
                                                        <option id="str_20582" value="19937">Mozartstraße</option>
                                                        <option id="str_20583" value="19939">Mühlenstraße</option>
                                                        <option id="str_20584" value="19945">Mühlweg</option>
                                                        <option id="str_20585" value="19939">Münchgasse</option>
                                                        <option id="str_20586" value="19935">Münzstraße</option>
                                                        <option id="str_403120" value="403107">Mwanzaweg</option>
                                                        <option id="str_20587" value="19937">Nachtigallenweg</option>
                                                        <option id="str_20588" value="19946">Neidertstraße</option>
                                                        <option id="str_20589" value="19940">Nelkenweg</option>
                                                        <option id="str_20590" value="19935">Neubaustraße</option>
                                                        <option id="str_20591" value="19943">Neubergstraße</option>
                                                        <option id="str_20592" value="19936">Neuenberg</option>
                                                        <option id="str_20593" value="19936">Neuenbrunner Weg</option>
                                                        <option id="str_20594" value="19936">Neuer Hafen</option>
                                                        <option id="str_20595" value="19946">Neunerplatz</option>
                                                        <option id="str_20596" value="19935">Neutorstraße</option>
                                                        <option id="str_20597" value="403103">Neydeckgasse</option>
                                                        <option id="str_20598" value="403103">Nigglweg</option>
                                                        <option id="str_20600" value="19944">Nikolausstraße</option>
                                                        <option id="str_20601" value="19937">Nopitschstraße</option>
                                                        <option id="str_505733" value="19937">Norbert-Glanzberg-Straße</option>
                                                        <option id="str_20602" value="19936">Nördliche Hafenstraße</option>
                                                        <option id="str_20603" value="19938">Nürnberger Straße</option>
                                                        <option id="str_20604" value="19940">Nußbaumweg</option>
                                                        <option id="str_20605" value="19938">Oberdürrbacher Straße</option>
                                                        <option id="str_20606" value="19945">Obere Heerbergstraße</option>
                                                        <option id="str_20607" value="19945">Obere Hofgasse</option>
                                                        <option id="str_20608" value="19935">Obere Johannitergasse</option>
                                                        <option id="str_20610" value="19945">Oberer Adelbergweg</option>
                                                        <option id="str_20611" value="19937">Oberer Bogenweg</option>
                                                        <option id="str_20612" value="19946">Oberer Burgweg</option>
                                                        <option id="str_20613" value="19944">Oberer Dallenbergweg</option>
                                                        <option id="str_20614" value="19939">Oberer Geibergweg</option>
                                                        <option id="str_20615" value="19939">Oberer Katzenbergweg</option>
                                                        <option id="str_20616" value="19939">Oberer Kirchbergweg</option>
                                                        <option id="str_20617" value="19940">Oberer Kirchplatz</option>
                                                        <option id="str_20618" value="19945">Oberer Kühlenberg</option>
                                                        <option id="str_20619" value="19944">Oberer Leitenweg</option>
                                                        <option id="str_20620" value="19935">Oberer Mainkai</option>
                                                        <option id="str_20621" value="19937">Oberer Neubergweg</option>
                                                        <option id="str_20622" value="19938">Oberer Schalksbergweg</option>
                                                        <option id="str_20623" value="19944">Oberer Steinbachweg</option>
                                                        <option id="str_20624" value="19936">Oberer Steinbergweg</option>
                                                        <option id="str_20625" value="19940">Oberer Torweinberg</option>
                                                        <option id="str_20609" value="19936">Obere Wand</option>
                                                        <option id="str_20626" value="19936">Oberhofstraße</option>
                                                        <option id="str_20627" value="19935">Oberthürstraße</option>
                                                        <option id="str_20628" value="19941">Odenwaldstraße</option>
                                                        <option id="str_20629" value="19935">Oeggstraße</option>
                                                        <option id="str_20630" value="19936">Öhlberg</option>
                                                        <option id="str_20631" value="19938">Ohmstraße</option>
                                                        <option id="str_20632" value="403107">Olympia-Promenade</option>
                                                        <option id="str_20633" value="403107">Osloer Straße</option>
                                                        <option id="str_20634" value="403107">Ossietzkystraße</option>
                                                        <option id="str_20635" value="19942">Ostpreußenstraße</option>
                                                        <option id="str_20636" value="403107">Otsustraße</option>
                                                        <option id="str_20637" value="19939">Otto-Fritz-Straße</option>
                                                        <option id="str_20638" value="19936">Otto-Hahn-Straße</option>
                                                        <option id="str_20639" value="19937">Otto-Nagler-Straße</option>
                                                        <option id="str_20640" value="19937">Otto-Richter-Straße</option>
                                                        <option id="str_20641" value="19941">Otto-Roth-Straße</option>
                                                        <option id="str_20642" value="401083">Otto-Stein-Straße</option>
                                                        <option id="str_20643" value="19935">Ottostraße</option>
                                                        <option id="str_20644" value="19941">Pacotistraße</option>
                                                        <option id="str_20645" value="19935">Paradeplatz</option>
                                                        <option id="str_20646" value="19936">Paradieshof</option>
                                                        <option id="str_20647" value="19936">Paradiesstraße</option>
                                                        <option id="str_20648" value="403108">Pariser Straße</option>
                                                        <option id="str_20649" value="19937">Parsevalstraße</option>
                                                        <option id="str_20650" value="403107">Pergamonweg</option>
                                                        <option id="str_20651" value="19938">Pestalozzistraße</option>
                                                        <option id="str_20652" value="19936">Peter-Haupt-Straße</option>
                                                        <option id="str_20653" value="19935">Peterpfarrgasse</option>
                                                        <option id="str_20654" value="19935">Peterplatz</option>
                                                        <option id="str_20655" value="19937">Peter-Schneider-Straße</option>
                                                        <option id="str_20656" value="19935">Peterstraße</option>
                                                        <option id="str_20657" value="19936">Peter-Wagner-Straße</option>
                                                        <option id="str_20658" value="19938">Petrinistraße</option>
                                                        <option id="str_20659" value="19936">Pfaffenbergstraße</option>
                                                        <option id="str_20660" value="19936">Pfaffenbergweg</option>
                                                        <option id="str_20661" value="19942">Pfalzstraße</option>
                                                        <option id="str_20662" value="19946">Pfarrer-Paul-Nützel-Straße</option>
                                                        <option id="str_20663" value="19935">Pfauengasse</option>
                                                        <option id="str_20664" value="19941">Philipp-Fasel-Str.</option>
                                                        <option id="str_20665" value="19935">Pickelstraße</option>
                                                        <option id="str_20666" value="401083">Pilziggrundstraße</option>
                                                        <option id="str_20667" value="403108">Place de Caen</option>
                                                        <option id="str_20668" value="19943">Platenstraße</option>
                                                        <option id="str_20669" value="19935">Plattnerstraße</option>
                                                        <option id="str_20670" value="19945">Pleichachgrund</option>
                                                        <option id="str_20671" value="19935">Pleicherkirchgasse</option>
                                                        <option id="str_20672" value="19935">Pleicherkirchplatz</option>
                                                        <option id="str_20673" value="19935">Pleicherpfarrgasse</option>
                                                        <option id="str_20674" value="19935">Pleicherschulgasse</option>
                                                        <option id="str_20675" value="19935">Pleichertorstraße</option>
                                                        <option id="str_20676" value="19935">Pleicherwall</option>
                                                        <option id="str_20677" value="19935">Pommergasse</option>
                                                        <option id="str_20678" value="19937">Popspfad</option>
                                                        <option id="str_20679" value="403107">Prager Ring</option>
                                                        <option id="str_20680" value="19935">Prymstraße</option>
                                                        <option id="str_20681" value="19941">Rabanus-Maurus-Straße</option>
                                                        <option id="str_20682" value="19946">Radulfsteige</option>
                                                        <option id="str_20683" value="19935">Raiffeisenstraße</option>
                                                        <option id="str_20684" value="19943">Randersackerer Straße</option>
                                                        <option id="str_20685" value="19939">Randersackerer Weg</option>
                                                        <option id="str_20686" value="19939">Rathausplatz Heidingsfeld</option>
                                                        <option id="str_20687" value="19940">Rebenstraße</option>
                                                        <option id="str_20688" value="19935">Reibeltgasse</option>
                                                        <option id="str_20689" value="403107">Reichenberger Straße</option>
                                                        <option id="str_20690" value="19938">Reiserstraße</option>
                                                        <option id="str_20691" value="19935">Reisgrubengasse</option>
                                                        <option id="str_20692" value="19941">Rembrandtstraße</option>
                                                        <option id="str_20693" value="19935">Rennweg</option>
                                                        <option id="str_20694" value="19935">Rennweger Ring</option>
                                                        <option id="str_20695" value="19939">Resenstraße</option>
                                                        <option id="str_20696" value="19939">Resenweg</option>
                                                        <option id="str_20697" value="19935">Residenzplatz</option>
                                                        <option id="str_20698" value="19935">Reuerergasse</option>
                                                        <option id="str_20699" value="19936">Reußenweg</option>
                                                        <option id="str_20700" value="19939">Reuterstraße</option>
                                                        <option id="str_20701" value="19938">Rhönstraße</option>
                                                        <option id="str_20702" value="19937">Richard-Strauß-Straße</option>
                                                        <option id="str_20703" value="19937">Richard-Wagner-Straße</option>
                                                        <option id="str_20704" value="19936">Riedelspfad</option>
                                                        <option id="str_20705" value="19941">Riedstraße</option>
                                                        <option id="str_20706" value="19943">Riemenschneiderstraße ger. Nr.</option>
                                                        <option id="str_20707" value="19935">Riemenschneiderstraße ung. Nr.</option>
                                                        <option id="str_20708" value="19938">Rimparer Steig</option>
                                                        <option id="str_20709" value="19938">Rimparer Straße</option>
                                                        <option id="str_20710" value="19936">Ringstraße</option>
                                                        <option id="str_20711" value="19935">Rittergasse</option>
                                                        <option id="str_20712" value="19941">Ritterstiftstraße</option>
                                                        <option id="str_20713" value="19938">Robert-Bunsen-Straße</option>
                                                        <option id="str_20714" value="19941">Robert-Kirchhoff-Straße</option>
                                                        <option id="str_20715" value="19938">Robert-Koch-Straße</option>
                                                        <option id="str_20716" value="403107">Rochesterstraße</option>
                                                        <option id="str_20717" value="19936">Rochusgasse</option>
                                                        <option id="str_404557" value="19941">Roland-Frank-Straße</option>
                                                        <option id="str_20718" value="403108">Römer Straße</option>
                                                        <option id="str_20719" value="19945">Römische Klinge</option>
                                                        <option id="str_20720" value="19935">Röntgenring</option>
                                                        <option id="str_20760" value="19937">Rosa-Buchbinder-Straße</option>
                                                        <option id="str_20721" value="19945">Rosa-Hahn-Straße</option>
                                                        <option id="str_20722" value="19935">Rosengasse</option>
                                                        <option id="str_20723" value="19938">Rosenmühlweg</option>
                                                        <option id="str_20724" value="19944">Roßbergweg</option>
                                                        <option id="str_20725" value="19940">Rotenburstraße</option>
                                                        <option id="str_20726" value="19946">Rotenhanstraße</option>
                                                        <option id="str_20727" value="19944">Rothäckerweg</option>
                                                        <option id="str_20728" value="19939">Röthenweg</option>
                                                        <option id="str_20729" value="19936">Rothofstraße</option>
                                                        <option id="str_20730" value="19944">Rothweg</option>
                                                        <option id="str_20731" value="19939">Rotkäppchenweg</option>
                                                        <option id="str_20732" value="19938">Rotkreuzsteige</option>
                                                        <option id="str_20733" value="19935">Rotkreuzstraße</option>
                                                        <option id="str_20734" value="19935">Rotlöwengasse</option>
                                                        <option id="str_20735" value="19935">Rotscheibengasse</option>
                                                        <option id="str_20736" value="19940">Rottenbauerer Grund</option>
                                                        <option id="str_20737" value="19935">Rottendorfer Straße 1-15</option>
                                                        <option id="str_20738" value="19937">Rottendorfer Straße 15a-Ende</option>
                                                        <option id="str_20739" value="19939">Rübezahlweg</option>
                                                        <option id="str_20740" value="19935">Rückermainstraße</option>
                                                        <option id="str_20741" value="19943">Rückertstraße</option>
                                                        <option id="str_20742" value="19935">Rüdigerstraße</option>
                                                        <option id="str_20743" value="19936">Rudolf-Clausius-Straße</option>
                                                        <option id="str_20744" value="19939">Ruppertsgasse</option>
                                                        <option id="str_506802" value="19937">Ruth-Pfau-Straße</option>
                                                        <option id="str_20745" value="19946">Saalgasse</option>
                                                        <option id="str_20746" value="403107">Salamancastraße</option>
                                                        <option id="str_20747" value="19937">Salvatorstraße</option>
                                                        <option id="str_20748" value="19941">Sandäcker</option>
                                                        <option id="str_20749" value="19937">Sandbergerstraße</option>
                                                        <option id="str_20750" value="19937">Sandbergstraße</option>
                                                        <option id="str_20751" value="19943">Sanderglacisstraße</option>
                                                        <option id="str_20752" value="19937">Sanderheimrichsleitenweg</option>
                                                        <option id="str_20753" value="19935">Sanderring</option>
                                                        <option id="str_20754" value="19937">Sanderrothstraße</option>
                                                        <option id="str_20755" value="19935">Sanderstraße</option>
                                                        <option id="str_20756" value="19939">Sandgrubenweg</option>
                                                        <option id="str_20757" value="19938">Sandweg</option>
                                                        <option id="str_20758" value="19935">Sartoriusstraße</option>
                                                        <option id="str_20759" value="19935">Scanzonistraße</option>
                                                        <option id="str_20761" value="19936">Schafhofstraße</option>
                                                        <option id="str_20762" value="19938">Schalksbergweg</option>
                                                        <option id="str_20763" value="19937">Schanzstraße</option>
                                                        <option id="str_20764" value="19946">Scharnhorststraße</option>
                                                        <option id="str_20765" value="19938">Scharoldstraße</option>
                                                        <option id="str_20766" value="403107">Schattbergweg</option>
                                                        <option id="str_20767" value="19943">Scheffelstraße</option>
                                                        <option id="str_20768" value="19937">Schellingstraße</option>
                                                        <option id="str_20769" value="19936">Schenkenschloßweg</option>
                                                        <option id="str_20770" value="19935">Schenkhof</option>
                                                        <option id="str_20771" value="19946">Scherenbergstraße</option>
                                                        <option id="str_20772" value="19943">Schießhausstraße</option>
                                                        <option id="str_20773" value="19938">Schiestlstraße</option>
                                                        <option id="str_20774" value="19935">Schildhof</option>
                                                        <option id="str_20775" value="19939">Schildweg</option>
                                                        <option id="str_20776" value="19943">Schillerstraße</option>
                                                        <option id="str_20777" value="19941">Schlehenweg</option>
                                                        <option id="str_20778" value="19940">Schleifweg</option>
                                                        <option id="str_20779" value="19942">Schlesierstraße</option>
                                                        <option id="str_20780" value="19937">Schlörstraße</option>
                                                        <option id="str_20781" value="403103">Schloßgasse</option>
                                                        <option id="str_20782" value="19940">Schloßhecke</option>
                                                        <option id="str_20783" value="19935">Schmalzmarkt</option>
                                                        <option id="str_20784" value="19939">Schneewittchenweg</option>
                                                        <option id="str_20785" value="19939">Schollergasse</option>
                                                        <option id="str_20786" value="19944">Schöllhammerweg</option>
                                                        <option id="str_20787" value="19935">Schönbornstraße</option>
                                                        <option id="str_20788" value="19935">Schönleinstraße</option>
                                                        <option id="str_20789" value="19935">Schönthalstraße</option>
                                                        <option id="str_20790" value="19941">Schöpf</option>
                                                        <option id="str_20791" value="19946">Schorkstraße</option>
                                                        <option id="str_20792" value="403103">Schottenanger</option>
                                                        <option id="str_20793" value="19940">Schulstraße</option>
                                                        <option id="str_20794" value="19940">Schulzenstraße</option>
                                                        <option id="str_20796" value="19935">Schürerstraße</option>
                                                        <option id="str_20797" value="19935">Schustergasse</option>
                                                        <option id="str_20798" value="19935">Schüttgasse</option>
                                                        <option id="str_20799" value="19941">Schützensteige</option>
                                                        <option id="str_20800" value="19942">Schwabenstraße</option>
                                                        <option id="str_20801" value="19935">Schwanenhof</option>
                                                        <option id="str_20802" value="19935">Schweinfurter Straße 2-13</option>
                                                        <option id="str_20803" value="19938">Schweinfurter Straße 26-Ende</option>
                                                        <option id="str_20804" value="19944">Sebastianisteig</option>
                                                        <option id="str_20805" value="19944">Sebastian-Kneipp-Weg</option>
                                                        <option id="str_20806" value="19937">Sebastian-Merkle-Straße</option>
                                                        <option id="str_20807" value="19946">Sedanstraße</option>
                                                        <option id="str_20808" value="19939">Seegartenweg</option>
                                                        <option id="str_20809" value="19935">Seelbergstraße</option>
                                                        <option id="str_20810" value="19941">Seepfad</option>
                                                        <option id="str_20811" value="19946">Seeweg</option>
                                                        <option id="str_20812" value="19939">Seilerstraße</option>
                                                        <option id="str_20813" value="19937">Seinsheimstraße</option>
                                                        <option id="str_20814" value="19935">Semmelstraße</option>
                                                        <option id="str_20815" value="19938">Senefelder Straße</option>
                                                        <option id="str_20816" value="19937">Seuffertstraße</option>
                                                        <option id="str_20817" value="19945">Siebenbürgenstraße</option>
                                                        <option id="str_20818" value="19943">Sieboldstraße</option>
                                                        <option id="str_20819" value="19936">Siedlungsstraße</option>
                                                        <option id="str_20820" value="19937">Silcherstraße</option>
                                                        <option id="str_20821" value="19935">Siligmüllerstraße</option>
                                                        <option id="str_20822" value="401083">Simon-Blenk-Weg</option>
                                                        <option id="str_20823" value="19937">Simon-Breu-Straße</option>
                                                        <option id="str_505738" value="19937">Skyline-Hill-Straße</option>
                                                        <option id="str_20824" value="19937">Sodenstraße</option>
                                                        <option id="str_20825" value="19941">Sonnenhang</option>
                                                        <option id="str_20826" value="19943">Sonnenstraße</option>
                                                        <option id="str_20827" value="19936">Sonnenweg</option>
                                                        <option id="str_20828" value="19941">Sonnleite</option>
                                                        <option id="str_20829" value="19943">Sophienstraße</option>
                                                        <option id="str_20830" value="403107">Spartaweg</option>
                                                        <option id="str_20831" value="19944">Spechtweg</option>
                                                        <option id="str_20832" value="19946">Spessartstraße</option>
                                                        <option id="str_20833" value="19935">Spiegelstraße</option>
                                                        <option id="str_20834" value="403103">Spitalgasse</option>
                                                        <option id="str_20835" value="19944">Spitalweg</option>
                                                        <option id="str_20836" value="19944">Spittelbergweg</option>
                                                        <option id="str_20837" value="403107">Spitztannenweg</option>
                                                        <option id="str_20844" value="19938">Ständerbühlstraße</option>
                                                        <option id="str_20845" value="19941">Stauferstraße</option>
                                                        <option id="str_20846" value="19940">Stauffenbergstraße</option>
                                                        <option id="str_20838" value="19935">St.-Benedikt-Straße</option>
                                                        <option id="str_20847" value="19939">Stegenturmgasse</option>
                                                        <option id="str_20848" value="19937">Stegerwaldstraße</option>
                                                        <option id="str_20849" value="19937">Steidlestraße</option>
                                                        <option id="str_20850" value="19939">Steigerfurtweg</option>
                                                        <option id="str_20851" value="19941">Steigerwaldstraße</option>
                                                        <option id="str_20852" value="19945">Steigstraße</option>
                                                        <option id="str_20853" value="403107">Steigwaldweg</option>
                                                        <option id="str_20854" value="19946">Steinachstraße</option>
                                                        <option id="str_20855" value="19944">Steinbachtal</option>
                                                        <option id="str_20856" value="19941">Steinbruchweg</option>
                                                        <option id="str_20857" value="19936">Steinburgstraße</option>
                                                        <option id="str_20858" value="19939">Steinhäuserstraße</option>
                                                        <option id="str_20859" value="19938">Steinheilstraße</option>
                                                        <option id="str_20860" value="19945">Steinlein</option>
                                                        <option id="str_20861" value="19935">Steinstraße</option>
                                                        <option id="str_20862" value="19939">Stengerstraße</option>
                                                        <option id="str_20863" value="19935">Stephanstraße</option>
                                                        <option id="str_20864" value="19937">Sterenstraße</option>
                                                        <option id="str_20865" value="19935">Sterngasse</option>
                                                        <option id="str_20866" value="19939">Sterntalerweg</option>
                                                        <option id="str_20867" value="19943">Stettiner Straße</option>
                                                        <option id="str_20868" value="19937">Steubenstraße</option>
                                                        <option id="str_20839" value="19945">St.-Jakobus-Straße</option>
                                                        <option id="str_20840" value="19936">St.-Josef-Straße</option>
                                                        <option id="str_20841" value="401083">St.-Lioba-Straße</option>
                                                        <option id="str_20869" value="403107">Stockholmer Straße</option>
                                                        <option id="str_20870" value="19937">Stöhrstraße</option>
                                                        <option id="str_20871" value="403107">Straßburger Ring</option>
                                                        <option id="str_20872" value="19944">Straße zum Waldfriedhof</option>
                                                        <option id="str_20873" value="506176">Straubmühlweg</option>
                                                        <option id="str_20842" value="19945">St.-Rochus-Straße</option>
                                                        <option id="str_20843" value="19936">St.-Stephan-Straße</option>
                                                        <option id="str_20874" value="19939">Stürzpfad</option>
                                                        <option id="str_20875" value="19939">Stuttgarter Straße</option>
                                                        <option id="str_20876" value="19942">Sudetenstraße</option>
                                                        <option id="str_20877" value="19936">Südliche Hafenstraße</option>
                                                        <option id="str_20878" value="19946">Talavera</option>
                                                        <option id="str_20879" value="401083">Talweg</option>
                                                        <option id="str_20880" value="19940">Tannenweg</option>
                                                        <option id="str_20881" value="19939">Taschenäckerweg</option>
                                                        <option id="str_20882" value="19941">Taschenpfad</option>
                                                        <option id="str_20883" value="403103">Tellsteige</option>
                                                        <option id="str_20884" value="19935">Textorstraße</option>
                                                        <option id="str_20885" value="19935">Theaterstraße</option>
                                                        <option id="str_20886" value="403107">Thebenweg</option>
                                                        <option id="str_20887" value="19937">Theodor-Boveri-Weg</option>
                                                        <option id="str_20888" value="19943">Theodor-Heuss-Damm</option>
                                                        <option id="str_20889" value="19943">Theodor-Körner-Straße</option>
                                                        <option id="str_20337" value="19937">Theresia-Winterstein-Straße</option>
                                                        <option id="str_20890" value="19935">Theresienstraße</option>
                                                        <option id="str_20891" value="19942">Thüringerstraße</option>
                                                        <option id="str_20892" value="19939">Tiefe Gasse</option>
                                                        <option id="str_20893" value="19935">Tiepolostraße</option>
                                                        <option id="str_20894" value="19943">Tilsiter Straße</option>
                                                        <option id="str_20895" value="403107">Tokiostraße</option>
                                                        <option id="str_20896" value="19939">Toräckerweg</option>
                                                        <option id="str_20897" value="19943">Traubengasse</option>
                                                        <option id="str_20898" value="19937">Trautenauer Straße</option>
                                                        <option id="str_20899" value="403107">Trojaweg</option>
                                                        <option id="str_20900" value="19935">Tröltschstraße</option>
                                                        <option id="str_20901" value="19940">Tulpenstraße</option>
                                                        <option id="str_20902" value="19935">Turmgasse</option>
                                                        <option id="str_20903" value="19943">Uhlandstraße</option>
                                                        <option id="str_20904" value="19940">Ulmenstraße</option>
                                                        <option id="str_20905" value="19935">Ulmer Hof</option>
                                                        <option id="str_20906" value="19937">Ulrichstraße</option>
                                                        <option id="str_20907" value="19936">Unterdürrbacher Straße</option>
                                                        <option id="str_20908" value="19935">Untere Bockgasse</option>
                                                        <option id="str_20909" value="19945">Untere Goldbergstraße</option>
                                                        <option id="str_20910" value="19945">Untere Heerbergstraße</option>
                                                        <option id="str_20911" value="19945">Untere Hofgasse</option>
                                                        <option id="str_20912" value="19935">Untere Johannitergasse</option>
                                                        <option id="str_20913" value="19945">Unterer Adelbergweg</option>
                                                        <option id="str_20914" value="19944">Unterer Dallenbergweg</option>
                                                        <option id="str_20915" value="19937">Unterer Hublandweg</option>
                                                        <option id="str_20916" value="19939">Unterer Katzenbergweg</option>
                                                        <option id="str_20917" value="19939">Unterer Kaulweg</option>
                                                        <option id="str_20918" value="19939">Unterer Kirchbergweg</option>
                                                        <option id="str_20919" value="19940">Unterer Kirchplatz</option>
                                                        <option id="str_20920" value="19945">Unterer Kühlenberg</option>
                                                        <option id="str_20921" value="19937">Unterer Neubergweg</option>
                                                        <option id="str_20922" value="19936">Unterer Steinbergweg</option>
                                                        <option id="str_20923" value="19940">Unterer Torweinberg</option>
                                                        <option id="str_20924" value="19936">Unterer Wandweg</option>
                                                        <option id="str_20925" value="19939">Unterer Weg</option>
                                                        <option id="str_20926" value="19938">Urlaubstraße</option>
                                                        <option id="str_20927" value="19935">Ursulinergasse</option>
                                                        <option id="str_20928" value="19944">V.-A.-Fischer-Weg</option>
                                                        <option id="str_20929" value="19935">Valentin-Becker-Straße</option>
                                                        <option id="str_20930" value="19935">Veitshöchheimer Straße 1-5 ung./2-30 ger. Nr.</option>
                                                        <option id="str_20931" value="19936">Veitshöchheimer Straße 7-Ende ung./32-Ende ger. Nr.</option>
                                                        <option id="str_20932" value="19945">Versbacher Röthe</option>
                                                        <option id="str_506464" value="506176">Versbacher Straße 3-33 ung. Nr. / 4-58 ger. Nr.</option>
                                                        <option id="str_506463" value="19942">Versbacher Straße 39-99 ung.</option>
                                                        <option id="str_20933" value="19945">Versbacher Straße 100-Ende</option>
                                                        <option id="str_20934" value="19938">Versbacher Straße 3-33 ung. Nr.</option>
                                                        <option id="str_20935" value="19942">Versbacher Straße 39-99 ung./4-92 ger. Nr.</option>
                                                        <option id="str_20936" value="19946">Vierter Siedlungsweg</option>
                                                        <option id="str_20937" value="19943">Virchowstraße</option>
                                                        <option id="str_20938" value="19941">Vogelsangweg</option>
                                                        <option id="str_20939" value="19937">Vogelweiderweg</option>
                                                        <option id="str_20940" value="19937">Voglerstraße</option>
                                                        <option id="str_20941" value="19937">Von-Luxburg-Straße</option>
                                                        <option id="str_20942" value="19946">Von-Mieg-Straße</option>
                                                        <option id="str_20943" value="19944">Vorderer Johannishof</option>
                                                        <option id="str_403117" value="19940">Wacholderweg</option>
                                                        <option id="str_20944" value="19938">Wagnerplatz</option>
                                                        <option id="str_20945" value="19938">Wagnerstraße</option>
                                                        <option id="str_20946" value="19940">Waidmannsau</option>
                                                        <option id="str_20947" value="19941">Waidmannsteige</option>
                                                        <option id="str_20948" value="19944">Waldkugelweg</option>
                                                        <option id="str_20949" value="19935">Wallgasse</option>
                                                        <option id="str_20950" value="19935">Wallkrone</option>
                                                        <option id="str_20951" value="19945">Walter-Stier-Straße</option>
                                                        <option id="str_20952" value="19936">Walther-Nernst-Straße</option>
                                                        <option id="str_20953" value="19937">Waltherstraße</option>
                                                        <option id="str_20954" value="19937">Walther-von-der-Vogelweide-Straße</option>
                                                        <option id="str_20955" value="19936">Wandweg</option>
                                                        <option id="str_20956" value="403107">Warschauer Straße</option>
                                                        <option id="str_20957" value="19939">Weg an der Ziegelhütte</option>
                                                        <option id="str_20958" value="19941">Weg zum Sportplatz</option>
                                                        <option id="str_20959" value="19939">Weg zur Neuen Welt</option>
                                                        <option id="str_20960" value="19946">Weg zur Zeller Waldspitze</option>
                                                        <option id="str_20961" value="19940">Weidenstraße</option>
                                                        <option id="str_20962" value="19936">Weinbergweg</option>
                                                        <option id="str_20963" value="19943">Weingartenstraße</option>
                                                        <option id="str_20964" value="19939">Weißbrückengraben</option>
                                                        <option id="str_20965" value="19940">Weißdornweg</option>
                                                        <option id="str_20966" value="19946">Weißenburgstraße</option>
                                                        <option id="str_20967" value="19936">Weißer Bildweg</option>
                                                        <option id="str_20968" value="19939">Wellhöferweg</option>
                                                        <option id="str_20969" value="19935">Welzstraße</option>
                                                        <option id="str_20970" value="19939">Wendelweg</option>
                                                        <option id="str_20971" value="19939">Wenzelstraße</option>
                                                        <option id="str_20972" value="19939">Werkingstraße</option>
                                                        <option id="str_20973" value="19938">Werner-von-Siemens-Straße 1-27</option>
                                                        <option id="str_20974" value="19941">Werner-von-Siemens-Straße 28-Ende</option>
                                                        <option id="str_20975" value="19938">Wickenmayerstraße</option>
                                                        <option id="str_20976" value="403107">Wiener Ring</option>
                                                        <option id="str_20977" value="19939">Wiesenweg</option>
                                                        <option id="str_20978" value="19946">Wilhelm-Dahl-Straße</option>
                                                        <option id="str_20979" value="19935">Wilhelm-Schwinn-Platz</option>
                                                        <option id="str_20980" value="19935">Wilhelmstraße</option>
                                                        <option id="str_20981" value="19936">Wilhelm-Wien-Straße</option>
                                                        <option id="str_20982" value="19939">Winterhäuser Straße</option>
                                                        <option id="str_20983" value="19940">Winterhäuser Weg</option>
                                                        <option id="str_20984" value="19944">Winterleitenweg</option>
                                                        <option id="str_20985" value="19935">Wirsbergstraße</option>
                                                        <option id="str_20986" value="19937">Wittelsbacherplatz</option>
                                                        <option id="str_20987" value="19937">Wittelsbacherstraße</option>
                                                        <option id="str_20988" value="19943">Wölffelstraße</option>
                                                        <option id="str_20989" value="19935">Wolfhartsgasse</option>
                                                        <option id="str_20990" value="19935">Wolframstraße</option>
                                                        <option id="str_20991" value="19940">Wolfskeelstraße</option>
                                                        <option id="str_20992" value="19935">Wöllergasse</option>
                                                        <option id="str_20993" value="19946">Wörthstraße</option>
                                                        <option id="str_20994" value="19946">Wredestraße</option>
                                                        <option id="str_403118" value="19940">Würzburger Höhe</option>
                                                        <option id="str_20996" value="19946">Ysenburgstraße</option>
                                                        <option id="str_20997" value="19940">Zehntgasse</option>
                                                        <option id="str_20998" value="19936">Zehnthofstraße</option>
                                                        <option id="str_21000" value="19946">Zellerangen-Forst</option>
                                                        <option id="str_20999" value="403103">Zeller Straße</option>
                                                        <option id="str_21001" value="19937">Zeppelinstraße</option>
                                                        <option id="str_21002" value="19935">Ziegelaustraße</option>
                                                        <option id="str_21003" value="19936">Ziegelhütte</option>
                                                        <option id="str_21004" value="19939">Zindelgasse</option>
                                                        <option id="str_21005" value="19935">Zinkhof</option>
                                                        <option id="str_21006" value="19938">Zinklesweg</option>
                                                        <option id="str_21007" value="19939">Zobelweg</option>
                                                        <option id="str_21008" value="19939">Zülbsgasse</option>
                                                        <option id="str_21009" value="19940">Zum Himmelreich</option>
                                                        <option id="str_21010" value="19936">Zum Sportplatz</option>
                                                        <option id="str_21011" value="19940">Zum Storchenbrünnlein</option>
                                                        <option id="str_21012" value="19945">Zum Tännig</option>
                                                        <option id="str_21013" value="19937">Zu-Rhein-Straße</option>
                                                        <option id="str_21014" value="19937">Zürnstraße</option>
                                                        <option id="str_403119" value="19940">Zur Würzburger Mehle</option>
                                                        <option id="str_21015" value="19937">Zweierweg</option>
                                                        <option id="str_21016" value="403103">Zweite Felsengasse</option>
                                                        <option id="str_21017" value="19946">Zweiter Siedlungsweg</option>
                                                        <option id="str_21018" value="19937">Zwerchgraben</option>
                                                        <option id="str_21019" value="19935">Zwinger</option>
"""

grouped_data = defaultdict(list)

pattern = re.compile(r'<option id="(?P<id>.*?)" value="(?P<value>.*?)">(?P<text>.*?)</option>')

for match in pattern.finditer(html_text):
    id_value = match.group('id')
    value = match.group('value')
    text = match.group('text')
    grouped_data[value].append({
        "id": id_value,
        "text": text
    })
json_data = json.dumps(grouped_data, indent=4, ensure_ascii=False)

with open('strasse.json', 'w', encoding='utf-8') as f:
    f.write(json_data)