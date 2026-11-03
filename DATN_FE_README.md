# 🎬 CineReserve — Cinema Ticket Booking & Seat Reservation Frontend

[![React](https://img.shields.io/badge/React-18.2-161B22?style=flat-square&logo=react&logoColor=61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.3-161B22?style=flat-square&logo=typescript&logoColor=3178C6)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-4.4-161B22?style=flat-square&logo=vite&logoColor=646CFF)](https://vitejs.dev/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.3-161B22?style=flat-square&logo=tailwindcss&logoColor=06B6D4)](https://tailwindcss.com/)
[![Redux Toolkit](https://img.shields.io/badge/Redux_Toolkit-1.9-161B22?style=flat-square&logo=redux&logoColor=764ABC)](https://redux-toolkit.js.org/)
[![Backend](https://img.shields.io/badge/Backend-Laravel_REST_API-161B22?style=flat-square&logo=laravel&logoColor=FF2D20)](https://github.com/phith75/PRO224_phithph22381)

A responsive, feature-rich web frontend for an end-to-end cinema management and ticket booking system. Built with React 18, TypeScript, and Vite, this client communicates with a high-performance **Laravel RESTful API backend** to handle real-time seat reservation locking, film schedules, user reviews, and automated payment gateway checkouts.

---

## 📌 Architecture & System Overview

CineReserve is designed with a decoupled client-server architecture:
- **Frontend (This Repository):** Single-page application (SPA) with typed API services, Redux Toolkit state persistence, and responsive UI components.
- **Backend API ([PRO224 / Laravel Backend](https://github.com/phith75/PRO224_phithph22381)):** Laravel REST API providing authentication via Laravel Sanctum, transactional seat cache locking, payment webhooks, and PDF/QR ticket generation.

```
┌────────────────────────────────┐            HTTP / JSON REST API            ┌────────────────────────────────┐
│   React 18 + TypeScript SPA    │ ◄────────────────────────────────────────► │    Laravel RESTful Backend     │
│   (Vite, Tailwind, Redux)      │   - Bearer Token Auth (Sanctum)            │    (PHP 8.x, MySQL, Sanctum)   │
│                                │   - Seat Hold Requests                     │                                │
│  - Film Browsing & Filters     │   - Payment Initialization                 │  - Concurrency Lock (cache_seat│
│  - Real-Time Seat Selection    │                                            │  - VNPay & MoMo IPN Handlers   │
│  - Checkout & Digital Tickets  │                                            │  - Revenue & Analytics Engine  │
└────────────────────────────────┘                                            └────────────────────────────────┘
```

---

## ✨ Key Features

1. **Interactive Seat Matrix & Reservation Locking:**
   - Visual cinema room seat layout with category-based seat pricing (Standard, VIP, Couple).
   - Temporary seat-holding state synchronized with backend cache (`/api/cache_seat`) to prevent concurrent double-booking during checkout.

2. **Film Schedule & Showtime Discovery:**
   - Multi-criteria browsing: filter by cinema branch, release status (Now Showing, Coming Soon), date, and showtime slots.
   - Detailed film view with trailer embeds, user ratings, and reviews.

3. **Integrated Payment Checkout:**
   - Dual payment gateway integration supporting **VNPay** and **MoMo** URL redirect workflows.
   - Internal coin wallet checkout option (`/api/coin_payment`) with refund capabilities.

4. **Digital Ticket & QR Generation:**
   - Post-payment confirmation page providing booking references and dynamic QR codes for on-site theater ticket validation.
   - Automated email dispatch integration via backend notification services.

5. **User Profile & Order Management:**
   - Booking history tracking with voucher discounts and status badges.
   - Authentication guard protecting user dashboard routes via JWT/Sanctum bearer tokens.

---

## 🛠️ Tech Stack

- **Core Framework:** React 18.2, TypeScript 5.3
- **Build Tool:** Vite 4.4
- **State Management:** Redux Toolkit 1.9, Redux Persist
- **Data Fetching:** Axios, React Query
- **UI & Styling:** Tailwind CSS 3.3, Ant Design 5.11, Material-UI 5.14
- **Date & Time:** Day.js, Moment.js, Date-fns
- **Icons & Visuals:** FontAwesome, Lucide / Heroicons, Ant Design Icons

---

## 📂 Project Structure

```
src/
├── apis/                  # Base Axios instance, interceptors, and file upload endpoints
├── assets/                # Static brand images, vectors, and stylesheets
├── components/            # Reusable UI elements (Modals, Seat Grids, Cards, Navigation)
├── configs/               # Application-level routes and global constants
├── guards/                # Route authorization guards for protected paths
├── hooks/                 # Custom React hooks (debounce, timer countdown, booking logic)
├── interface/             # TypeScript type declarations and API response interfaces
├── pages/                 # Top-level route views (Home, FilmDetail, Booking, Checkout, Profile)
├── service/               # Strongly-typed API client services matching backend endpoints
│   ├── book_ticket.service.ts
│   ├── chairs.service.ts
│   ├── films.service.ts
│   ├── payMoMo.service.ts
│   ├── payVnpay.service.ts
│   ├── seatkeping.service.ts
│   └── ...
├── store/                 # Redux Toolkit slices (Auth, BookingState, Cart, Vouchers)
└── utils/                 # Formatting utilities (currency, dates, error handlers)
```

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18.x or higher
- npm, yarn, or pnpm
- Running instance of the [Cinema Laravel Backend](https://github.com/phith75/PRO224_phithph22381) (default: `http://127.0.0.1:8080`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/phith752003/DATN_FE.git
   cd DATN_FE
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   ```env
   VITE_API_BASE_URL=http://127.0.0.1:8080/api
   ```

4. **Start Development Server:**
   ```bash
   npm run dev
   ```
   The application will be accessible at `http://localhost:5173`.

5. **Build for Production:**
   ```bash
   npm run build
   ```

---

## 🔗 Related Repositories

- **Backend API Service:** [phith75/PRO224_phithph22381](https://github.com/phith75/PRO224_phithph22381) — Laravel 10 REST API powering this frontend.

---

## 📜 License

This project was developed as a graduation capstone project at FPT Polytechnic College. Released under the [MIT License](LICENSE).

