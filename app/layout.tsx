import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Excel · Paso a paso",
  description: "Aprende Excel con casos de oficina técnica, ejercicios descargables e integraciones.",
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
    <html lang="es">
      <body className="antialiased">{children}</body>
    </html>
  );
}
