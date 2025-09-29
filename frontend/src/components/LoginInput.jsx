
export const LoginInput = ({title, type}) => {
  return (
    <>
      <div>
        <div>{title}</div>
        <div>
          <input type={type} />
        </div>
      </div>
    </>
  );
};
