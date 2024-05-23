class DefaultConfig():
    #backbone
    pretrained=True
    freeze_stage_1=False
    freeze_bn=False

    #fpn
    fpn_out_channels=256
    use_p5=True
    
    #head
    class_num=6
    use_GN_head=True
    prior=0.01
    add_centerness=True
    cnt_on_reg=True

    #training
    strides=[8,16,32,64,128]
    limit_range=[[-1,64],[64,128],[128,256],[256,512],[512,999999]]

    #inference
    score_threshold=0.25
    nms_iou_threshold=0.6
    max_detection_boxes_num=1000