import { app } from "../../scripts/app.js";

function findWidgetByName(node, name) {
	return node.widgets.find((w) => w.name === name);
}

function updateNodeHeight(node) {
	node.setSize([node.size[0], node.computeSize()[1]]);
}

const origProps = {};
function toggleWidget(node, widget, show = false, suffix = "") {
	if (!widget) {		
		return;
	}

	if (!origProps[widget.name]) {
		origProps[widget.name] = { origType: widget.type, origComputeSize: widget.computeSize };	
	}

	const origSize = node.size;
	widget.type = show ? origProps[widget.name].origType : "CustomSchedulerHidden" + suffix;
	widget.computeSize = show ? origProps[widget.name].origComputeSize : () => [0, -4];
	widget.linkedWidgets?.forEach(w => toggleWidget(node, w, ":" + widget.name, show));
	
	const height = show ? Math.max(node.computeSize()[1], origSize[1]) : node.size[1];
	node.setSize([node.size[0], height]);	
}

function toggleSigmaWidgets(node, steps) {
	let number_to_show = steps + 1
	for (let i = 0; i < number_to_show; i++) {
		toggleWidget(node, findWidgetByName(node, 'sigma_' + i), true)
	}
	for (let i = number_to_show; i <= 25; i++) {
		toggleWidget(node, findWidgetByName(node, 'sigma_' + i), false)
	}
	updateNodeHeight(node)
}

app.registerExtension({
	name: "comfy.CustomScheduler",
	
	nodeCreated(node) {
		if (node.getTitle() !== "CustomScheduler") {
			return;
		}

		const widget = findWidgetByName(node, "steps")
		if (!widget) {
			return;
		}

		let widgetValue = widget.value
		Object.defineProperty(widget, 'value', {
			get() {
				return widgetValue;
			},
			set(newValue) {
				if (newValue !== widgetValue) {
					toggleSigmaWidgets(node, newValue)
					widgetValue = newValue
				}
			}
		});

		toggleSigmaWidgets(node, widgetValue)
	}
});
