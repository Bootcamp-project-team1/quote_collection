import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import TempPage from "./pages/TempPage";

const RootLayout = () => {
  return (
    <div className="relative min-h-screen flex justify-center items-center bg-main-green">
      <div className="relative">
        <NavBar />
        <div className="relative z-10 w-[50vw] min-h-[90vh] bg-main-white shadow-2xl rounded-lg">
          <main className="p-8 md:p-12 text-center text-black">
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
      { index: true, element: <TempPage output={"메인"} /> },
      {
        element: <Outlet />,
        children: [
          { path: "temp", element: <TempPage output={1} /> },
          { path: "temp2", element: <TempPage output={2} /> },
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
