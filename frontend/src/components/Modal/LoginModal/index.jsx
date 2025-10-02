import { Link, useNavigate } from "react-router-dom";
import { LoginInput } from "../../LoginInput";

const LoginModal = ({ setIsLogin, setIsOpen }) => {
  const navigation = useNavigate();
  const handleSubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const email = form.email.value;
    const password = form.password.value;

    try {
      const response = await fetch("http://localhost:8081/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          username: email,
          password: password,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Login failed");
      }

      const data = await response.json();
      localStorage.setItem("accessToken", data.access_token);
      alert("로그인 완료");
      setIsLogin(true);
      setIsOpen(false);
      navigation("/");
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <>
      {/* <div className="bg-gray-50 w-[100vw] absolute"></div> */}
      <div className="bg-amber-500 ">
        <div>LOGIN</div>

        <form className="space-y-4" onSubmit={handleSubmit}>
          <LoginInput title="email" type="email" name="email" />
          <div>
            <LoginInput title="password" type="password" name="password" />
            <div>
              <button>login</button>
            </div>
          </div>
        </form>

        <div>
          <div>아직 회원이 아니시라면?</div>
          <div>
            <Link to="/register">join us</Link>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginModal;
