import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import { Logo } from "./components/NavBar/layout/logo";
import { MainPage } from "./pages/MainPage";
import { LoginBar } from "./components/NavBar/layout/LoginBar";
import { Bookmark } from "./pages/Bookmark";
import { Write } from "./pages/Write";
import { Mypage } from "./pages/Mypage";
import LoginModal from "./components/Modal/LoginModal";
import { useState } from "react";
import { Popular } from "./pages/MainPage/layout/Popular";

const RootLayout = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isLogIn, setIsLogin] = useState(false);

  return (
    <div className="relative">
      <div className="min-h-screen relative justify-center justify-items-center bg-main-green">
        <div className="relative">
          <NavBar />
          <div className="relative z-10 w-[60vw] min-h-[90vh] mt-11 bg-main-white shadow-2xl rounded-lg">
            <div className=" absolute flex  justify-center items-center">
              {isOpen && (
                <LoginModal setIsOpen={setIsOpen} setIsLogin={setIsLogin} />
              )}
            </div>
            <LoginBar
              setIsLogin={setIsLogin}
              isLogIn={isLogIn}
              setIsOpen={setIsOpen}
            />
            <main className="p-8 md:p-12 text-center text-black">
              <Logo/>
              <Outlet />
            </main>
          </div>
        </div>
      </div>
    </div>
  );
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      { index: true, element: <MainPage mode={'book'}/> },
      {
        element: <Outlet />,
        children: [
          { path: "/movie", element: <MainPage mode={'movie'}  /> },
          { path: "/drama", element: <MainPage mode={'drama'} /> },
          { path: "/bookmark", element: <Bookmark /> },
          { path: "/write", element: <Write /> },
          { path: "/mypage", element: <Mypage /> },
          { path: "/popular", element: <Popular/>},
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
