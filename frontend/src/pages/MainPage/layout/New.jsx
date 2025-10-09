export const New =({newQuote})=>{
    
    return(
        <>
        <div className="flex-col flex items-center mb-12">
          <div className="mt-14 mb-4 text-3xl">NEW</div>
          {newQuote.map((quote)=>(
            <div key={quote.id}className="mt-5 w-11/12 bg-new-bg h-full pt-5 pb-5 text-center rounded-lg shadow-lg">
            <div>{quote.content}</div>
          </div>
          ))}
        </div>
        </>
    );
}