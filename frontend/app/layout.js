import { Inter } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/components/wrapper/theme-provider";
import Navbar from "@/components/custom/Navbar";
import Footer from "@/components/custom/Footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <Navbar />
          <div className=" min-h-[80vh] ">{children}</div>
          <Footer />
        </ThemeProvider>
      </body>
    </html>
  );
}
