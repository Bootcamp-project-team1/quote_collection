import { createBrowserRouter, RouterProvider, Outlet } from "react-router-dom";
import NavBar from "./components/NavBar";
import TempPage from "./pages/TempPage";

/** 이곳에 라우팅과 상관 없이 모든 페이지에 들어갈 컴포넌트 들을 넣어주세요
 * eg. NavBar, 타이틀(로고), 로그인 여부 체크 등등
 */
const RootLayout = () => {
  return (
    <div className="relative flex min-h-[80vh] min-w-[70vw] shadow-2xl rounded-sm bg-[#E5E8E1]">
      <header>
        <NavBar className="absolute left-0 top-1/2 -translate-y-1/2 flex flex-col z-20 rotate-270 origin-left" />
      </header>
      <main className="p-8 md:p-12 text-center text-black relative z-20 ">
        <Outlet />
      </main>
    </div>
  );
};

/**
 * 이곳에 Route 설정
 */
const router = createBrowserRouter([
  {
    path: "/", // 메인 페이지
    element: <RootLayout />,
    children: [
      { index: true, element: <TempPage output={"메인"} /> }, // 나중에 메인(랜딩) 페이지 넣을곳
      {
        element: <Outlet />,
        children: [
          // 이곳에 페이지들 추가
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
