import { Link, Router, useNavigate } from "react-router-dom";
import { LoginInput } from "../../LoginInput";

const LoginModal = ({ setIsLogin, setIsOpen }) => {
  const navigation = useNavigate();
  
  const handleSubmit = (e) => {
    e.preventDefault();
    alert("로그인 완료");
    setIsLogin(true);
    setIsOpen(false);
    navigation("/");
  };

  return (
    <>
      {/* <div className="flex justify-items-center"></div> */}
      <div className="bg-main-green/80 h-[300px] w-[300px] rounded-sm flex-col flex items-start md:items-center justify-between md:justify-center">
        <div className="text-custom-div text-3xl mb-5 cursor-pointer">LOGIN</div>

        <form className="space-y-4 " onSubmit={handleSubmit}>
          <LoginInput title="email" type="email" />
          <div className="flex items-center mb-5">
            <LoginInput title="password" type="password" />
            <button className="bg-custom-div w-[50px] ml-3 h-[30px] flex justify-center items-center">
              login
            </button>
            <div></div>
          </div>
        </form>

        <div className="flex">
          <div className="mr-3 text-white">아직 회원이 아니시라면?</div>
          <div className="text-custom-bold-font underline">
            <Link href="#">join us</Link>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginModal;
