import SigninInput from "../SigninInput";

export const Signup = () => {
  const handlesubmit = (e) => {
    e.preventDefault();
  };
  return (
    <>
      <div className="mt-10  flex-col items-center justify-center">
        <div className="mb-10 text-custom-basic-font text-3xl">Signup</div>

        <form className="flex-col items-center justify-center" onSubmit={handlesubmit}>
          <SigninInput title="이름" type="name" name="name" />
          <div className="">
            <SigninInput title="이메일" type="email" name="email" />
            <SigninInput title="비밀번호" type="password" name="password" />
            <SigninInput
              title="비밀번호 확인"
              type="passwordConfirm"
              name="password confirm"
            />
            <div className="mt-5">
              <button
                type="submit"
                className="bg-custom-search mr-3 w-[80px] h-[30px]"
              >
                Cancle
              </button>
              <button
                type="submit"
                className="bg-custom-pink w-[80px] h-[30px]"
              >
                Confirm
              </button>
            </div>
          </div>
        </form>
      </div>
    </>
  );
};
