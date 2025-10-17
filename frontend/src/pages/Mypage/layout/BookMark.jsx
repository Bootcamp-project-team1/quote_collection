import { useState } from "react";
import { useBookmarkTree } from "../../../hooks/useBookmarkTree";
import FolderNode from "../../../components/FolderNode";
import NameModal from "../../../components/Modal/NameModal.jsx";

export function BookMark() {
  const { tree, addAtId, createFolderAt } = useBookmarkTree();
  const [modalOpen, setModalOpen] = useState(false);
  const [targetId, setTargetId] = useState(null);

  const openModalAt = (id) => {
    setTargetId(id);
    setModalOpen(true);
  };

  const confirmCreate = (name) => {
    if (targetId) createFolderAt(targetId, name);
    setModalOpen(false);
    setTargetId(null);
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-medium mb-4">Bookmark</h1>
      <FolderNode node={tree} addAtId={addAtId} onRequestCreateAt={openModalAt} />
      <NameModal open={modalOpen} onClose={() => setModalOpen(false)} onConfirm={confirmCreate} />
    </div>
  );
}
