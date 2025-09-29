import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import { Logo } from "./components/NavBar/layout/logo";
import { MainPage } from "./pages/MainPage";
import { LoginBar } from "./components/NavBar/layout/LoginBar";
import { SearchBar } from "./components/NavBar/layout/SearchBar";
import { Bookmark } from "./pages/Bookmark";
import { Upload } from "./pages/Upload";
import { Mypage } from "./pages/Mypage";
import { MoviePage } from "./pages/MoviePage";
import { DramaPage } from "./pages/DramaPage";

const RootLayout = () => {
  return (
    <div className="min-h-screen relative justify-center justify-items-center bg-main-green">
      <div className="relative">
        <NavBar />
        <div className="relative z-10 w-[60vw] min-h-[90vh] mt-11 bg-main-white shadow-2xl rounded-lg">
           <LoginBar />
          <main className="p-8 md:p-12 text-center text-black">
              <Logo />
              <div className="flex justify-center">
                <SearchBar/>
              </div>
            <Outlet />
          </main>
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
      { index: true, element: <MainPage/> },
      {
        element: <Outlet />,
        children: [
          { path: "movie", element: <MoviePage/> },
          { path: "drama", element: <DramaPage /> },
          { path: "bookmark",element:<Bookmark/>},
          { path: "upload",element:<Upload/>},
          { path: "mypage", element:<Mypage/>},
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
