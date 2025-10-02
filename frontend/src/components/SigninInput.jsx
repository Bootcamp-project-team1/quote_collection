import React from 'react';

const SigninInput = ({title, type}) => {
    return (
    <>
      <div>
        <div className="text-white">{title}</div>
        <div>
          <input type={type} className="bg-white"/>
        </div>
      </div>
    </>
  );
};

export default SigninInput;