import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Trace — Evidence-first research",
  description: "Turn complex questions into answers you can verify.",
  other: {
    "codex-preview": "development",
  },
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
