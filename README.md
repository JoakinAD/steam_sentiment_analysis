# 🎮 Steam Review Scraper

A Python-based web scraper designed to extract structured review data from the Steam Store. The goal of this project is to create a rich, custom dataset for downstream machine learning tasks—especially sentiment analysis—while showcasing my skills in web scraping, data extraction, and Python development.

> ⚠️ This project was built entirely by me from scratch, without using AI-generated code. All development was done through manual research, reading documentation, and forums like Stack Overflow—just good old-fashioned coding. Generative AI tools (like ChatGPT) were only used for non-essential tasks such as improving the wording of this README. The core purpose of the project was learning and showcasing my own technical skills.


---

## 🚀 Features

- Scrapes the first 60 most relevant games from Steam's store listing.
- For each game, extracts:
  - 🎮 Game title
  - 🏷️ Genre(s)
  - 📝 10 most recent **positive** reviews
  - 📝 10 most recent **negative** reviews
  - 🌟 10 **top-rated** positive reviews
  - 🌟 10 **top-rated** negative reviews

- For each review, extracts:
  - 👍 Number of users who marked it as "helpful"
  - 😂 Number of users who marked it as "funny"
  - 🏅 Number of Steam awards received
  - ✅ Whether it's marked as "Recommended" or "Not Recommended"
  - ⏱️ User's playtime at time of review
  - 🗒️ Full review text

---

## 🛠️ Tech Stack

- **Python 3.x**
- **BeautifulSoup** for HTML parsing
- **Requests** for HTTP communication

---

## 🧠 Purpose and Learning Objectives

This project was built from scratch as a hands-on way to deepen my understanding of:

- Web scraping at scale
- Navigating dynamic HTML structures
- Designing scalable data pipelines
- Building reusable, clean, and documented Python code

No external code generators, including ChatGPT, were used in writing the core functionality of this project.

---

## 📦 Planned Features

- [ ] Export scraped data to **JSON**, **CSV**, and **PostgreSQL**
- [ ] Docker container for easy deployment and reproducibility
- [ ] Command-line interface (CLI) for custom configurations
- [ ] Improved error handling and retry mechanisms for request failures

---

## 🚧 Limitations

- The scraper works with publicly available data and does not bypass any form of authentication or CAPTCHA.
- Because Steam’s structure may change, future updates might be needed to maintain scraping functionality.

---

## 🤝 License

This project is licensed under the **GNU General Public License v3.0**. You are free to use, modify, and distribute this software under the terms of the [GPLv3 license](https://www.gnu.org/licenses/gpl-3.0.en.html).