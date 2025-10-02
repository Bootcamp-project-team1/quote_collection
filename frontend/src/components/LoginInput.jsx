
export const LoginInput = ({ title, type, name }) => {
  return (
    <>
      <div>
        <div>{title}</div>
        <div>
          <input type={type} name={name} />
        </div>
      </div>
    </>
  );
};
