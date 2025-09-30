import { NavLink } from "react-router-dom";
import LoginModal from "../../Modal/LoginModal";

export const LoginBar = ({ setIsOpen, isLogIn, setIsLogin }) => {
  const handleLogout = (e) => {
    e.preventDefault();
    alert("로그아웃 되었습니다");
    setIsLogin(false);
  };

  return (
    <>
      <nav className="float-right mr-3 mt-3 text-sm z-20">
        <NavLink className="mr-3" to="/BookMark">
          Bookmark
        </NavLink>
        <NavLink className="mr-3" to="/Write">
          write
        </NavLink>
        {isLogIn ? (
          <>
            <NavLink className="mr-3" to="/Mypage">
              mypage
            </NavLink>
            <span className="mr-3" onClick={handleLogout}>
              logout
            </span>
          </>
        ) : (
          <>
            <span className="mr-3" onClick={() => setIsOpen(true)}>
              login
            </span>
          </>
        )}
      </nav>
    </>
  );
};
