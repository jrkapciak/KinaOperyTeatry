# KinaOperyTeatry

Głównym założeniem projektu jest stworzenie portalu przedstawiające dane dotyczące wydarzeń związanych z kulturą na terenie Krakowa. Obecie aplikacja pobiera dane z Opery Krakowskiej i prezentuje ja na mapie przy użyciu biblioteki Leaflet.

Projekt opiera się na danych pozyskanych za pomocą scrapperów (biblioteka Scrapy) oraz wprowadzonych ręcznie przez administratora. Zastosowanie webscrappingu pozwala zmiejszyć nakład wymaganej prac, koniecznej do prezentacji aktualnych informacji z wielu źródeł. Pobrane dane gromadzone są w bazie danych PostgreSQL, które następnie są przy użyciu Django Rest API udostępniane. Wykorzystanie wspomnianej technologii REST umożlwia oddzielenie częsci front-endowej od back-endu co pozytywnie wpływa na utrzymanie oraz przyszły rozwój projektu. W najbliższej przyszłość (grudzień 2017) zostanie udoskonalony interface użytkownika o możliwość wyboru dnia dodatkowo planowane jest wprowadzenie kolejnego scrappera. Następnie zostanie wprowadzony moduł odpowiedzialny za rejstrację użytkowników oraz dodawanie przez nich treści.
