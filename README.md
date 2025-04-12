# Anime Lord - Advanced Telegram File Sharing Bot 🚀

![Anime Lord Banner](https://via.placeholder.com/1200x400.png?text=Anime+Lord+-+File+Sharing+Bot)  
*A powerful and feature-rich Telegram bot designed for seamless file sharing with advanced functionalities.*

---

## 📖 Overview

**Anime Lord** is a Telegram bot built to simplify file sharing while offering advanced features like force subscription, auto-delete, custom welcome messages, broadcast capabilities, and more. It is designed to be user-friendly for both admins and regular users, with an intuitive menu system to avoid repetitive command typing.

This bot is perfect for communities, content creators, or anyone looking to share files securely and efficiently on Telegram.

---

## ✨ Features

- **File Sharing**: Generate shareable links for files with a single command (`/genlink`).
- **Batch File Upload**: Save multiple files at once using `/batch`.
- **Force Subscription**: Require users to join specific channels before using the bot.
- **Auto-Delete**: Automatically delete files after a set time (default: 20 minutes).
- **Custom Welcome Messages**: Set custom welcome messages with random images using `/cst_welcome_msg`.
- **Copyright Warning**: Display a copyright warning message for forwarded files, customizable via `/cws`.
- **Interactive Menu**: Access all commands via an inline keyboard menu (`/menu`), with separate options for admins and users.
- **Broadcast**: Send messages to all users with `/broadcast` (admin-only).
- **Admin Controls**: Manage bot settings, view user stats, and restart the bot (admin-only).
- **MongoDB Integration**: Store user data and bot settings persistently.
- **Multi-Platform Deployment**: Deploy on Termux, Koyeb, Heroku, Railway, or VPS.

---

## 📋 Prerequisites

Before setting up the bot, ensure you have the following:

- **Python 3.9+** installed on your system.
- A **Telegram Bot Token** (get it from [@BotFather](https://t.me/BotFather)).
- **MongoDB Atlas** account for database storage (optional, but recommended).
- Channel IDs for file storage and force subscription.
- Admin Telegram user ID for bot administration.
- Basic knowledge of Git and command-line usage.

---

## ⚙️ Setup Instructions

Follow these steps to set up the bot locally or deploy it to a cloud platform.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/MyFileSharingBot.git
cd MyFileSharingBot
