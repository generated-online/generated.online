<template>
    <v-card class="info-container">
        <v-container :class="['mb-16',{'mt-8': $vuetify.breakpoint.mdAndUp}]">
            <h1 class="text-span boldy" style="font-size:3em">Was ist das hier?</h1>
            <br>
            <h2 class="project-description boldy">
                <span class=text-span>
                    Stell dir vor jemand schaut sich ganz viele Rezepte an,
                    filtert alle unbedeutenten und schlechten Rezepte raus und erstellt
                    neue Rezepte basierend auf diesem Datensatz.
                </span>
                <br>
                <br>
                <span class=text-span>
                    Genau das haben wir gemacht!
                </span>
                <br>
                <br>
                <span class=text-span>
                    Aber anstatt uns selber neue Rezepte zu
                    überlegen, haben wir eine Künstliche Intelligenz (<b>KI</b>) darauf trainiert
                    möglichst gute Rezepte zu generieren.
                </span>
                <br>
                <br>
                <span class=text-span>
                    Die Ergebnisse reichen von sehr lustig oder unkochbar zu einwandfrei
                    vorstellbar als Rezept aus einem Kochbuch.
                </span>
                <br>
                <br>
                <span class=text-span>
                    Wenn dich unser Code interessiert schau doch mal auf unserem
                    <v-btn class="black-button" href="https://github.com/generated-online/generated.online">
                        <v-icon class="mr-2" size="30"> mdi-github </v-icon> Github-Repo
                    </v-btn>
                    vorbei und lass einen Stern da!
                </span>
            </h2>
        </v-container>
        <br>
        <!-- Disclaimer -->
        <h2 class="boldy-no-animation" @click="showDisclaimer = !showDisclaimer">Bedingungen und Konditionen</h2>
        <br>
        <v-container class="boldy-no-animation" :class="{hide: !showDisclaimer}">
            <p>Willkommen bei generated.online!</p>
            <p>Diese Bedingungen und Konditionen umreißen die Regeln und Bestimmungen für die Nutzung der Website von
                generated.online, die sich unter generated.online.</p>
            <p> befindet. Mit dem Zugriff auf diese Website gehen wir davon aus, dass Sie diese Bedingungen und
                Konditionen akzeptieren. Verwenden Sie generated.online nicht weiter, wenn Sie nicht damit einverstanden
                sind, alle auf dieser Seite genannten Bedingungen und Konditionen zu akzeptieren. Unsere Allgemeinen
                Geschäftsbedingungen wurden mit Hilfe des <a href='https://www.termsandconditionsgenerator.com'>Terms
                    And Conditions Generator</a>.</p>
            <p> Die folgende Terminologie gilt für diese Allgemeinen Geschäftsbedingungen, die Datenschutzerklärung und
                den Haftungsausschluss sowie alle Vereinbarungen: 'Kunde', 'Sie' und 'Ihr' bezieht sich auf Sie, die
                Person, die sich auf dieser Website einloggt und sich an die Geschäftsbedingungen des Unternehmens hält.
                'Das Unternehmen', 'Wir', 'Sie', 'Wir', 'Unser' und 'Uns' bezieht sich auf unser Unternehmen. 'Partei',
                'Parteien' oder 'Wir', bezieht sich sowohl auf den Kunden als auch auf uns selbst. Alle Begriffe
                beziehen sich auf das Angebot, die Annahme und die Berücksichtigung der Zahlung, die erforderlich ist,
                um den Prozess unserer Unterstützung für den Kunden in der am besten geeigneten Weise durchzuführen, um
                die Bedürfnisse des Kunden in Bezug auf die Bereitstellung der angegebenen Dienstleistungen des
                Unternehmens in Übereinstimmung mit und vorbehaltlich des geltenden niederländischen Rechts zu erfüllen.
                Jegliche Verwendung der obigen Terminologie oder anderer Wörter im Singular, Plural, in Großbuchstaben
                und/oder er/sie oder sie werden als austauschbar angesehen und beziehen sich daher auf dasselbe.</p>
            <h3><strong>Cookies</strong></h3>
            <p>Wir verwenden Cookies. Mit dem Zugriff auf generated.online haben Sie der Verwendung von Cookies in
                Übereinstimmung mit den Datenschutzrichtlinien von generated.online zugestimmt.</p>
            <p>Die meisten interaktiven Websites verwenden Cookies, damit wir bei jedem Besuch die Daten des Benutzers
                abrufen können. Cookies werden von unserer Website verwendet, um die Funktionalität bestimmter Bereiche
                zu ermöglichen und den Besuchern unserer Website zu erleichtern. Einige unserer Partner/Werbepartner
                können ebenfalls Cookies verwenden.</p>
            <h3><strong>Lizenz</strong></h3>
            <p> Sofern nicht anders angegeben, sind generated.online und/oder seine Lizenzgeber Eigentümer der geistigen
                Eigentumsrechte für das gesamte Material auf generated.online. Alle Rechte an geistigem Eigentum sind
                vorbehalten. Sie dürfen auf dieses Material von generated.online für Ihren eigenen persönlichen Gebrauch
                zugreifen, wobei Sie den in diesen Bedingungen festgelegten Einschränkungen unterliegen.</p>
            <p> Sie dürfen nicht:</p>
            <ul>
                <li>Material von generated.online veröffentlichen. </li>
                <li>Material von generated.online verkaufen, vermieten oder unterlizenzieren, reproduzieren, duplizieren
                    oder kopieren. </li>
                <li>Inhalt von generated.online weiterverbreiten</li>
            </ul>
            <p>Diese Vereinbarung beginnt mit dem Datum dieses Vertrags.</p>
            <p>Teile dieser Website bieten den Benutzern die Möglichkeit, Meinungen und Informationen in bestimmten
                Bereichen der Website zu veröffentlichen und auszutauschen. generated.online filtert, bearbeitet,
                veröffentlicht oder überprüft Kommentare nicht, bevor sie auf der Website erscheinen. Die Kommentare
                spiegeln nicht die Ansichten und Meinungen von generated.online, seinen Agenten und/oder angeschlossenen
                Unternehmen wider. Kommentare spiegeln die Ansichten und Meinungen der Person wider, die ihre Ansichten
                und Meinungen veröffentlicht. Soweit nach geltendem Recht zulässig, ist generated.online nicht haftbar für
                die Kommentare oder für Haftungsansprüche, Schäden oder Kosten, die durch die Nutzung und/oder
                Veröffentlichung und/oder das Erscheinen der Kommentare auf dieser Website verursacht und/oder erlitten
                werden.</p>
            <p>generated.online behält sich das Recht vor, alle Kommentare zu überwachen und alle Kommentare zu entfernen,
                die als unangemessen, beleidigend oder als Verstoß gegen diese Nutzungsbedingungen angesehen werden
                können. </p>
            <p>
                <p>Sie garantieren und sichern dies zu: </p>
                <ul>
                    <li>Sie sind berechtigt, die Kommentare auf unserer Website zu veröffentlichen und verfügen über
                        alle erforderlichen Lizenzen und Einverständniserklärungen, um dies zu tun;</li>
                    <li>Die Kommentare verletzen keine geistigen Eigentumsrechte, einschließlich und ohne Einschränkung
                        Urheberrechte, Patente oder Marken Dritter; </li>
                    <li>Die Kommentare enthalten kein diffamierendes, verleumderisches, beleidigendes, anstößiges,
                        unanständiges oder anderweitig rechtswidriges Material, das eine Verletzung der Privatsphäre
                        darstellt;</li>
                    <li>Die Kommentare werden nicht verwendet, um Geschäfte oder Gewohnheiten zu fördern oder
                        kommerzielle Aktivitäten oder rechtswidrige Aktivitäten zu präsentieren. </li>
                </ul>
                <p>Sie gewähren generated.online hiermit eine nicht-exklusive Lizenz, Ihre Kommentare in allen Formen,
                    Formaten oder Medien zu verwenden, zu reproduzieren, zu bearbeiten und anderen zu gestatten, diese
                    zu verwenden, zu reproduzieren und zu bearbeiten. </p>
                <h3><strong>iFrames</strong></h3>
                <p>Ohne vorherige Genehmigung und schriftliche Erlaubnis dürfen Sie keine Frames um unsere Webseiten
                    erstellen, die die visuelle Präsentation oder das Erscheinungsbild unserer Website in irgendeiner
                    Weise verändern. </p>
                <h3><strong>Inhaltshaftung</strong></h3>
                <p>Wir übernehmen keine Verantwortung für Inhalte, die auf Ihrer Website erscheinen. Sie stimmen zu, uns
                    gegen alle Ansprüche, die auf Ihrer Website entstehen, zu schützen und zu verteidigen. Es dürfen
                    keine Links auf einer Website erscheinen, die als verleumderisch, obszön oder kriminell
                    interpretiert werden können oder die Rechte Dritter verletzen, anderweitig verletzen oder die
                    Verletzung oder anderweitige Verletzung von Rechten Dritter befürworten.</p>
                <h3><strong>Ihre Privatsphäre</strong></h3>
                <p>Bitte lesen Sie die Datenschutzrichtlinie</p>
                <h3><strong>Rechtsvorbehalt >/strong></strong></h3>
                <p>Wir behalten uns das Recht vor, Sie aufzufordern, alle Links oder einen bestimmten Link zu unserer
                    Website zu entfernen. Sie erklären sich damit einverstanden, auf Anfrage sofort alle Links zu
                    unserer Website zu entfernen. Wir behalten uns außerdem das Recht vor, diese Geschäftsbedingungen
                    und ihre Verlinkungsrichtlinien jederzeit zu ändern. Durch die kontinuierliche Verlinkung zu unserer
                    Website erklären Sie sich damit einverstanden, an diese Verlinkungsbedingungen gebunden zu sein und
                    sie zu befolgen.</p>
                <h3><strong>Entfernung von Links von unserer Website</strong></h3>
                <p> Sollten Sie einen Link auf unserer Website finden, der aus irgendeinem Grund anstößig ist, können
                    Sie uns jederzeit kontaktieren und informieren. Wir werden Anfragen zur Entfernung von Links prüfen,
                    sind aber nicht verpflichtet, Ihnen direkt zu antworten.</p>
                <p> Wir garantieren nicht, dass die Informationen auf dieser Website korrekt sind, wir garantieren nicht
                    ihre Vollständigkeit oder Genauigkeit; noch versprechen wir, dass die Website verfügbar bleibt oder
                    dass das Material auf der Website auf dem neuesten Stand gehalten wird. </p>
                <h3><strong>Disclaimer</strong></h3>
                <p>Im größtmöglichen gesetzlich zulässigen Umfang schließen wir alle Zusicherungen, Gewährleistungen und
                    Bedingungen in Bezug auf unsere Website und die Nutzung dieser Website aus. Nichts in diesem
                    Haftungsausschluss wird:</p>
                <ul>
                    <li> unsere oder Ihre Haftung für Tod oder Körperverletzung einschränken oder ausschließen;</li>
                    <li> unsere oder Ihre Haftung für Betrug oder betrügerische Falschdarstellung einschränken oder
                        ausschließen;</li>
                    <li> unsere oder Ihre Haftung in einer Weise einschränken oder ausschließen, die nach geltendem
                        Recht nicht zulässig ist; oder</li>
                    <li> unsere oder Ihre Haftung ausschließen, die nach geltendem Recht nicht ausgeschlossen werden
                        darf. </li>
                </ul>
                <p> Die Haftungsbeschränkungen und -verbote, die in diesem Abschnitt und an anderer Stelle in diesem
                    Haftungsausschluss festgelegt sind: (a) unterliegen dem vorstehenden Absatz; und (b) regeln alle
                    Haftungen, die sich aus dem Haftungsausschluss ergeben, einschließlich Haftungen aus Vertrag,
                    unerlaubter Handlung und wegen Verletzung gesetzlicher Pflichten.</p>
                <p> Solange die Website und die Informationen und Dienstleistungen auf der Website kostenlos zur
                    Verfügung gestellt werden, haften wir nicht für Verluste oder Schäden jeglicher Art.</p>
        </v-container>
        <br>
        <!-- Imprint -->
        <h2 class="boldy-no-animation" @click="showImprint = !showImprint">Impressum</h2>
        <br>
        <v-container class="boldy-no-animation" :class="{hide: !showImprint}">
            <p>Angaben gemäß § 5 TMG</p>
            <p>generated.online <br> Arnpeckstr 11<br> 81545 München <br> </p>
            <p> <strong>Vertreten durch: </strong><br> Moritz Wolf<br> </p>
            <p><strong>Kontakt:</strong> <br> E-Mail: <a
                    href="mailto:contact@generated.online">contact@generated.online</a></br></p>
            <p><strong>Haftungsausschluss: </strong><br><br><strong>Haftung für Inhalte</strong><br><br> Die Inhalte
                unserer Seiten wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität
                der Inhalte können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG
                für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG
                sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde
                Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit
                hinweisen. Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den
                allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem
                Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden
                Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.<br><br><strong>Haftung für
                    Links</strong><br><br> Unser Angebot enthält Links zu externen Webseiten Dritter, auf deren Inhalte
                wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen.
                Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten
                verantwortlich. Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße
                überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente
                inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer
                Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links
                umgehend entfernen.<br><br><strong>Urheberrecht</strong><br><br> Die durch die Seitenbetreiber
                erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die
                Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des
                Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers. Downloads
                und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet. Soweit die
                Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet.
                Insbesondere werden Inhalte Dritter als solche gekennzeichnet. Sollten Sie trotzdem auf eine
                Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden
                von Rechtsverletzungen werden wir derartige Inhalte umgehend
                entfernen.<br><br><strong>Datenschutz</strong><br><br> Die Nutzung unserer Webseite ist in der Regel
                ohne Angabe personenbezogener Daten möglich. Soweit auf unseren Seiten personenbezogene Daten
                (beispielsweise Name, Anschrift oder eMail-Adressen) erhoben werden, erfolgt dies, soweit möglich, stets
                auf freiwilliger Basis. Diese Daten werden ohne Ihre ausdrückliche Zustimmung nicht an Dritte
                weitergegeben. <br> Wir weisen darauf hin, dass die Datenübertragung im Internet (z.B. bei der
                Kommunikation per E-Mail) Sicherheitslücken aufweisen kann. Ein lückenloser Schutz der Daten vor dem
                Zugriff durch Dritte ist nicht möglich. <br> Der Nutzung von im Rahmen der Impressumspflicht
                veröffentlichten Kontaktdaten durch Dritte zur Übersendung von nicht ausdrücklich angeforderter Werbung
                und Informationsmaterialien wird hiermit ausdrücklich widersprochen. Die Betreiber der Seiten behalten
                sich ausdrücklich rechtliche Schritte im Falle der unverlangten Zusendung von Werbeinformationen, etwa
                durch Spam-Mails, vor.<br> <br><br><strong>Google Analytics</strong><br><br> Diese Website benutzt
                Google Analytics, einen Webanalysedienst der Google Inc. ("Google"). Google Analytics verwendet sog.
                "Cookies", Textdateien, die auf Ihrem Computer gespeichert werden und die eine Analyse der Benutzung der
                Website durch Sie ermöglicht. Die durch den Cookie erzeugten Informationen über Ihre Benutzung dieser
                Website (einschließlich Ihrer IP-Adresse) wird an einen Server von Google in den USA übertragen und dort
                gespeichert. Google wird diese Informationen benutzen, um Ihre Nutzung der Website auszuwerten, um
                Reports über die Websiteaktivitäten für die Websitebetreiber zusammenzustellen und um weitere mit der
                Websitenutzung und der Internetnutzung verbundene Dienstleistungen zu erbringen. Auch wird Google diese
                Informationen gegebenenfalls an Dritte übertragen, sofern dies gesetzlich vorgeschrieben oder soweit
                Dritte diese Daten im Auftrag von Google verarbeiten. Google wird in keinem Fall Ihre IP-Adresse mit
                anderen Daten der Google in Verbindung bringen. Sie können die Installation der Cookies durch eine
                entsprechende Einstellung Ihrer Browser Software verhindern; wir weisen Sie jedoch darauf hin, dass Sie
                in diesem Fall gegebenenfalls nicht sämtliche Funktionen dieser Website voll umfänglich nutzen können.
                Durch die Nutzung dieser Website erklären Sie sich mit der Bearbeitung der über Sie erhobenen Daten
                durch Google in der zuvor beschriebenen Art und Weise und zu dem zuvor benannten Zweck
                einverstanden.<br><br><strong>Google AdSense</strong><br><br> Diese Website benutzt Google Adsense,
                einen Webanzeigendienst der Google Inc., USA ("Google"). Google Adsense verwendet sog. "Cookies"
                (Textdateien), die auf Ihrem Computer gespeichert werden und die eine Analyse der Benutzung der Website
                durch Sie ermöglicht. Google Adsense verwendet auch sog. "Web Beacons" (kleine unsichtbare Grafiken) zur
                Sammlung von Informationen. Durch die Verwendung des Web Beacons können einfache Aktionen wie der
                Besucherverkehr auf der Webseite aufgezeichnet und gesammelt werden. Die durch den Cookie und/oder Web
                Beacon erzeugten Informationen über Ihre Benutzung dieser Website (einschließlich Ihrer IP-Adresse)
                werden an einen Server von Google in den USA übertragen und dort gespeichert. Google wird diese
                Informationen benutzen, um Ihre Nutzung der Website im Hinblick auf die Anzeigen auszuwerten, um Reports
                über die Websiteaktivitäten und Anzeigen für die Websitebetreiber zusammenzustellen und um weitere mit
                der Websitenutzung und der Internetnutzung verbundene Dienstleistungen zu erbringen. Auch wird Google
                diese Informationen gegebenenfalls an Dritte übertragen, sofern dies gesetzlich vorgeschrieben oder
                soweit Dritte diese Daten im Auftrag von Google verarbeiten. Google wird in keinem Fall Ihre IP-Adresse
                mit anderen Daten der Google in Verbindung bringen. Das Speichern von Cookies auf Ihrer Festplatte und
                die Anzeige von Web Beacons können Sie verhindern, indem Sie in Ihren Browser-Einstellungen "keine
                Cookies akzeptieren" wählen (Im MS Internet-Explorer unter "Extras > Internetoptionen > Datenschutz >
                Einstellung"; im Firefox unter "Extras > Einstellungen > Datenschutz > Cookies"); wir weisen Sie jedoch
                darauf hin, dass Sie in diesem Fall gegebenenfalls nicht sämtliche Funktionen dieser Website voll
                umfänglich nutzen können. Durch die Nutzung dieser Website erklären Sie sich mit der Bearbeitung der
                über Sie erhobenen Daten durch Google in der zuvor beschriebenen Art und Weise und zu dem zuvor
                benannten Zweck einverstanden.</p><br> Impressum vom <a
                href="https://www.impressum-generator.de">Impressum Generator</a> der <a
                href="https://www.kanzlei-hasselbach.de/standorte/bonn/">Kanzlei Hasselbach, Bonn</a>
            <!-- Privacy -->
        </v-container>
        <!-- Privacy -->
        <br>
        <h2 class="boldy-no-animation" @click="showPrivacy = !showPrivacy">Datenschutz für generated.online</h2>
        <br>
        <v-container class="boldy-no-animation" :class="{hide: !showPrivacy}">
            <p>Bei generated.online, erreichbar über generated.online, ist die Privatsphäre unserer Besucher eine unserer
                Hauptprioritäten. Dieses Dokument zum Datenschutz enthält Arten von Informationen, die von generated.online
                gesammelt und aufgezeichnet werden, sowie die Art und Weise, wie wir sie verwenden.</p>
            <p> Sollten Sie weitere Fragen haben oder weitere Informationen über unsere Datenschutzrichtlinien
                benötigen, zögern Sie nicht, uns per E-Mail zu kontaktieren: privacy@generated.online</p>
            <h2>Allgemeine Datenschutzverordnung (GDPR)</h2>
            <p> Wir sind für die Verarbeitung Ihrer Informationen verantwortlich.</p>
            <p> Die rechtliche Grundlage für die Erfassung und Verwendung der in dieser Datenschutzrichtlinie
                beschriebenen persönlichen Daten hängt von den von uns erfassten persönlichen Daten und dem spezifischen
                Kontext ab, in dem wir die Daten erfassen:</p>
            <ul>
                <li>generated.online muss einen Vertrag mit Ihnen erfüllen</li>
                <li>Sie haben generated.online die Erlaubnis dazu erteilt:</li>
                <li> Die Verarbeitung Ihrer persönlichen Daten erfolgt in generated.online legitimen Interessen:</li>
                <li>generated.online muss dem Gesetz entsprechen:</li>
            </ul>
            <p>p>generated.online wird Ihre persönlichen Daten nur so lange aufbewahren, wie es für die in dieser
                Datenschutzerklärung dargelegten Zwecke erforderlich ist. Wir werden Ihre Daten in dem Maße aufbewahren
                und verwenden, wie dies zur Erfüllung unserer gesetzlichen Verpflichtungen, zur Beilegung von
                Streitigkeiten und zur Durchsetzung unserer Richtlinien erforderlich ist.</p>
            <p> Wenn Sie im Europäischen Wirtschaftsraum (EWR) ansässig sind, haben Sie bestimmte Datenschutzrechte.
                Wenn Sie darüber informiert werden möchten, welche persönlichen Daten wir über Sie speichern, und wenn
                Sie möchten, dass diese aus unseren Systemen entfernt werden, kontaktieren Sie uns bitte. Unsere
                Datenschutzrichtlinie wurde mit Hilfe des <a href='https://www.gdprprivacypolicy.net.com/'>GDPR Privacy
                    Policy Generator</a>.</p>
            <p> Unter bestimmten Umständen haben Sie folgende Datenschutzrechte:</p>
            <ul>
                <li>Das Recht, auf die Informationen, die wir über Sie haben, zuzugreifen, sie zu aktualisieren oder zu
                    löschen. </li>
                <li>
                <li>Das Recht auf Berichtigung.</li>
                <li>Das Recht auf Einspruch.</li>
                <li>Das Recht auf Einschränkung.</li>
                <li>Das Recht auf Datenportabilität</li>
                <li>Das Recht auf Widerruf der Zustimmung</li>
            </ul>
            <h2>Log Files</h2>
            <p>generated.online folgt einem Standardverfahren der Verwendung von Logfiles. Diese Dateien protokollieren
                Besucher, wenn sie Websites besuchen. Alle Hosting-Unternehmen tun dies und einen Teil der Analysen der
                Hosting-Dienste. Die von den Protokolldateien gesammelten Informationen umfassen
                Internet-Protokolladressen (IP-Adressen), Browser-Typ, Internet Service Provider (ISP), Datums- und
                Zeitstempel, verweisende Seiten und möglicherweise die Anzahl der Klicks. Diese sind nicht mit
                Informationen verknüpft, die eine persönliche Identifizierung ermöglichen. Der Zweck der Informationen
                besteht darin, Trends zu analysieren, die Website zu verwalten, die Bewegungen der Benutzer auf der
                Website zu verfolgen und demographische Informationen zu sammeln.</p>
            <h2>Cookies und Web Beacons</h2>
            <p>Wie jede andere Website verwendet generated.online 'Cookies'. Diese Cookies werden verwendet, um
                Informationen zu speichern, einschließlich der Präferenzen der Besucher und der Seiten auf der Website,
                auf die der Besucher zugegriffen oder die er besucht hat. Die Informationen werden verwendet, um die
                Benutzererfahrung zu optimieren, indem der Inhalt unserer Webseite auf den Browsertyp des Besuchers
                und/oder andere Informationen abgestimmt wird.</p>
            <h2>Datenschutzrichtlinien</h2>
            <P>In dieser Liste finden Sie die Datenschutzrichtlinien für jeden der Werbepartner von plsreturn. me.</p>
            <p>
                <p>Anzeigenserver oder Werbenetzwerke von Drittanbietern verwenden Technologien wie Cookies, JavaScript
                    oder Web Beacons, die in ihren jeweiligen Anzeigen und Links verwendet werden, die auf generated.online
                    erscheinen und direkt an den Browser der Benutzer gesendet werden. Sie erhalten automatisch Ihre
                    IP-Adresse, wenn dies geschieht. Diese Technologien werden verwendet, um die Wirksamkeit ihrer
                    Werbekampagnen zu messen und/oder um den Werbeinhalt, den Sie auf den von Ihnen besuchten Websites
                    sehen, zu personalisieren.</p>
                <p>Hinweis, dass generated.online keinen Zugang zu oder Kontrolle über diese Cookies hat, die von
                    Drittanbietern verwendet werden. </p>
                <h2>Datenschutzrichtlinien von Drittanbietern</h2>
                <p>p>generated.online's Datenschutzrichtlinien gelten nicht für andere Werbetreibende oder Websites. Daher
                    raten wir Ihnen, für genauere Informationen die jeweiligen Datenschutzrichtlinien dieser
                    Drittanbieter-Anzeigenserver zu konsultieren. Sie können deren Praktiken und Anweisungen über das
                    Opt-out bestimmter Optionen enthalten. Eine vollständige Liste dieser Datenschutzrichtlinien und
                    ihrer Links finden Sie hier: Links zu den Datenschutzrichtlinien.</p>
                <p>Sie können die Cookies über Ihre individuellen Browser-Optionen deaktivieren. Ausführlichere
                    Informationen über die Cookie-Verwaltung mit bestimmten Webbrowsern finden Sie auf den jeweiligen
                    Websites der Browser. Was sind Cookies?</p>
                <h2>Informationen für Kinder</h2>
                <p> Ein weiterer Teil unserer Priorität ist der zusätzliche Schutz von Kindern bei der Nutzung des
                    Internets. Wir ermutigen Eltern und Erziehungsberechtigte, ihre Online-Aktivitäten zu beobachten, an
                    ihnen teilzunehmen und/oder sie zu überwachen und zu leiten.</p>
                <p>
                    <p>generated.online sammelt nicht wissentlich personenbezogene Daten von Kindern unter 13 Jahren. Wenn
                        Sie der Meinung sind, dass Ihr Kind diese Art von Informationen auf unserer Website zur
                        Verfügung gestellt hat, empfehlen wir Ihnen dringend, uns umgehend zu kontaktieren, und wir
                        werden uns nach besten Kräften bemühen, solche Informationen umgehend aus unseren Aufzeichnungen
                        zu entfernen.</p>
                    <h2>Nur Online-Datenschutzrichtlinie</h2>
                    <p>Unsere Datenschutzrichtlinie (erstellt bei GDPRPrivacyPolicy.net) gilt nur für unsere
                        Online-Aktivitäten und ist gültig für Besucher unserer Website in Bezug auf die Informationen,
                        die sie in generated.online mitgeteilt und/oder gesammelt haben. Diese Richtlinie gilt nicht für
                        Informationen, die offline oder über andere Kanäle als diese Website gesammelt werden. <a
                            href='https://gdprprivacypolicy.net'>Unsere GDPR-Datenschutzerklärung</a> wurde aus dem
                        GDPR-Datenschutzerklärungs-Generator generiert.</p>
                    <h2>Zustimmung</h2>
                    <p> Durch die Nutzung unserer Website erklären Sie sich hiermit mit unserer Datenschutzerklärung
                        einverstanden und stimmen ihren Bedingungen zu.</p>

        </v-container>
        <br>
        
    </v-card>
</template>

<script>
    import EmojieBackground from "@/components/EmojieBackground"

    export default {
        data() {
            return {
                showPrivacy: false,
                showImprint: false,
                showDisclaimer: false,
            }
        },
        components: {
            EmojieBackground
        },
        name: "info",
        created() {
            this.$emit('shareText', "Schau dir diese coolen von einer KI generierten Rezepte an!");
            this.$emit('recipe', null);
        }
    };
</script>

<style scoped>
    .project-description {
        text-align: justify;
        margin-bottom: 1em;
    }
    .hide {
        display: none;
    }

    h2.boldy-no-animation {
        cursor: pointer;
    }

    .boldy-no-animation {
        background: black;
        padding: 20px !important;
        border-radius: 30px !important;
        color: var(--bg-color) !important;
    }
</style>