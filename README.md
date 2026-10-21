# League Player Analyzer

A Python-based League of Legends player analysis tool that retrieves gameplay data using the Riot Games API and calculates performance statistics.

The project aims to evolve into a data-driven player recommendation system using statistical analysis, data mining, and machine learning.

## About the Project

League Player Analyzer is a personal project developed to python and applications of data analysis, and eventually machine learning using real League of Legends gameplay data.

The application currently runs through a command-line interface and allows users to retrieve their recent match history and analyze individual performance.

Future development will focus on identifying player strengths, analyzing champion performance, and providing personalized recommendations.

## Current Features

- **Riot ID Lookup:** Accepts a Riot ID (`GameName#TagLine`) and retrieves the player's PUUID.
- **Input Validation:** Rejects incorrectly formatted Riot IDs.
- **Match History Retrieval:** Fetches the player's 10 most recent matches using Riot's Match-V5 API.
- **Win Rate Calculation:** Calculates the player's win percentage across retrieved matches.
- **KDA Analysis:** Calculates individual-match and overall KDA ratios.
- **Champion Performance Grouping:** Groups match records by champion for champion-specific analysis.
- **Champion Mastery Retrieval:** Retrieves champion mastery information through Riot's API.
- **Champion ID Mapping:** Converts numerical champion IDs into champion names using Riot's Data Dragon.
- **Unit Testing:** Uses pytest to verify calculations and handle edge cases.

The application uses separate modules for API communication, player data processing, and statistical analysis.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Riot Games API | Player and match data |
| Data Dragon | Champion information |
| Requests | HTTP requests |
| python-dotenv | Environment variable management |
| pytest | Unit testing |
| Git & GitHub | Version control |

**Module responsibilities:**

- `main.py` — Application entry point and workflow coordination.
- `player.py` — Riot ID validation and player PUUID retrieval.
- `matches.py` — Match history retrieval and participant extraction.
- `champions.py` — Champion information and ID-to-name mapping.
- `analysis.py` — Win rate, KDA, and champion-specific statistical calculations.
- `config.py` — API key and request configuration.
- `tests/` — Automated unit tests.

## Development Roadmap

### Phase 1 — Core Player Analysis

- [x] Set up Python project and GitHub repository.
- [x] Integrate the Riot Games API.
- [x] Retrieve player PUUID using Riot ID.
- [x] Retrieve recent match history.
- [x] Extract individual participant information.
- [x] Calculate player win rate.
- [x] Calculate individual and overall KDA.
- [x] Group matches by champion.
- [x] Add initial unit tests.
- [ ] Complete error handling for invalid accounts and API rate limits.
- [ ] Add champion-specific performance summaries.

### Phase 2 — Data Storage and Visualization

- [ ] Implement a SQLite database.
- [ ] Store match history to reduce repeated API requests.
- [ ] Add additional gameplay statistics.
- [ ] Create an interactive player dashboard.
- [ ] Visualize win rates, KDA trends, and champion performance.

### Phase 3 — Data Science and Machine Learning

- [ ] Introduce Bayesian win-rate estimation.
- [ ] Analyze champion performance while accounting for sample size.
- [ ] Explore player playstyle clustering.
- [ ] Develop a personalized champion recommendation system.
- [ ] Compare statistical and machine learning approaches.
- [ ] Evaluate model performance using historical match data.

## Disclaimer

League Player Analyzer is an independent educational project and is not endorsed by Riot Games.

League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc.

Gameplay data is accessed using Riot Games' official APIs and is subject to Riot's developer policies.