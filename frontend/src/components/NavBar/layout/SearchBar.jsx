export const SearchBar=()=>{
    return(
        <div className="bg-main-beige p-8 pt-14 w-4/5 mt-14 rounded-xl shadow-xl">
        <input type="text" placeholder="검색어를 입력하세요" className="w-3/4 p-2 h-7 border-b-2  focus:outline-none"/>
        <button className="border-2 p-2 ml-3 rounded-md">search</button>
        </div>

    );
}