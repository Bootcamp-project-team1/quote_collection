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
      {/* <div className="bg-gray-50 w-[100vw] absolute"></div> */}
      <div className="bg-amber-500 ">
        <div>LOGIN</div>

        <form className="space-y-4" onSubmit={handleSubmit}>
          <LoginInput title="email" type="email" />
          <div>
            <LoginInput title="password" type="password" />
            <div>
              <button>login</button>
            </div>
          </div>
        </form>

        <div>
          <div>아직 회원이 아니시라면?</div>
          <div>
            <Link href="#">join us</Link>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginModal;
