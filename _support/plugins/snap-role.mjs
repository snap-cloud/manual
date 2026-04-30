// plugins/snap-role.mjs
const snapRole = {
  name: "snap",
  doc: "Render the Snap! brand mark with styled bang.",
  body: { type: String, doc: "Ignored; always emits 'Snap!'" },
  run() {
    return [{
      type: "span", class: "snap-brand",
      children: [
        { type: "text", value: "Snap" },
        { type: "emphasis", children: [{ type: "text", value: "!" }] },
      ],
    }];
  },
};
export default { name: "Snap brand", roles: [snapRole] };
