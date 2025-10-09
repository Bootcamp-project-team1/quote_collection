import { useNavigate } from "react-router-dom";

export const RecommendDetail =()=>{

    const navigation = useNavigate();
    
    const onDetail=(id)=>{
        navigation('/detail',{state:{key:id}})
    }

    /**dummy data */
    const q = [{'content':'1'},{'content':'2'},{'content':'3'}];
    
    return(
        <>
        <div className="flex-col flex items-center mb-12">
          <div className="mt-16 mb-4 text-3xl">User Based Recommend</div>
          {q.map((quote)=>(
            <div key={quote.id}className="mt-5 cursor-pointer w-11/12 border-2 border-main-green h-full pt-5 pb-5 text-center rounded-lg shadow-lg" onClick={() => onDetail(quote.id)}>
            <div>{quote.content}</div>
          </div>
          ))}
        </div>
        </>
    );
}