import React from 'react';

const SigninInput = ({title, type}) => {
    return (
    <>
      <div className=" flex justify-end-safe items-center">
        <div className='mr-3 mb-3'>{title}</div>
        <div>
          <input type={type} className="w-[300px] bg-white rounded-md shadow-md focus:shadow-lg focus:outline-none p-1 m-2"/>
        </div>
      </div>
    </>
  );
};

export default SigninInput;